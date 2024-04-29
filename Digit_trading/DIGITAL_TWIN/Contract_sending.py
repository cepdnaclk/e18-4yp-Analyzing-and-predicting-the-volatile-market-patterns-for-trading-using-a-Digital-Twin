
import sys
sys.path.append('.')
import asyncio
import os
from deriv_api import DerivAPI

async def sample_calls(random_number,stake,app_id,api_token): 
    
    api_token = os.getenv('DERIV_TOKEN', api_token)

    if len(api_token) == 0:

        sys.exit("DERIV_TOKEN environment variable is not set")

    try :

        api = DerivAPI(app_id=app_id)

        connection_established = await api.ping({'ping': 1})

        if connection_established['ping']:
            # print(connection_established['ping'],"--------connection_established--------\n")
            print("connected  with deriv platform.........\n")
                
        active_symbols = await api.active_symbols({"active_symbols": "brief", "product_type": "basic"})

        authorize = await api.authorize(api_token)
        
        cached_active_symbols = await api.cache.active_symbols({"active_symbols": "brief", "product_type": "basic"})

        assets = await api.cache.asset_index({"asset_index": 1})

        execute = True

        while execute:

            starting_balance = await api.balance()

            proposal = await api.proposal({
                
                "proposal": 1,
                "amount": stake ,
                "barrier": random_number,
                "basis": "stake",
                "contract_type": "DIGITMATCH",
                "currency": "USD",
                "duration": 1,
                "duration_unit": "t",
                "symbol": "R_100"
            })

            

            response = await api.buy({"buy": proposal.get('proposal').get('id'), "price": stake})
                
            if response and response.get('buy') and response.get('buy').get('contract_id'):

                contract_id = response.get('buy').get('contract_id')
                    
                
                # Assuming the contract ID is now correctly retrieved, proceed with the call
                poc = await api.proposal_open_contract({

                        "proposal_open_contract": 1,
                        "subscribe": 1,
                        "contract_id": contract_id
                })
                    
                # Check if contract is closed and print profit/loss
                if poc and poc.get('proposal_open_contract'):

                    current_spot = poc.get('proposal_open_contract').get('current_spot')

                    barrier = poc.get('proposal_open_contract').get('barrier')

                    contract_type = poc.get('proposal_open_contract').get('contract_type')

                    await asyncio.sleep(5)

                    ending_balance = await api.balance()

                    profit = ending_balance.get('balance')['balance'] - starting_balance.get('balance')['balance'] 

                    if profit > 0 :

                        print( "digit : ",random_number,"  stake : ",stake, "  profit : ",profit )  
                        print("\n")    

                    else :

                        print( "digit : ",random_number,"  stake : ",stake, "  profit : ",profit )  
                        print("\n")


                    return profit 
                                

                else:

                    print("Buy order failed or contract ID not found in response.")

                            
            else:
                    
                print("No response")

    except :

            print("Timed out. Reconnecting...")

            await sample_calls(random_number,stake,app_id,api_token)  # Reconnect on timeout


