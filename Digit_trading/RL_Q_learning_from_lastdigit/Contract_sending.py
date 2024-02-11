
import sys
sys.path.append('.')
import asyncio
import os
from deriv_api import DerivAPI
import websockets
from random import randint
import numpy as np
from main import main
from train import train

app_id = 52537

api_token = os.getenv('DERIV_TOKEN', 'HfVygCcTGmZJWuu')

if len(api_token) == 0:

    sys.exit("DERIV_TOKEN environment variable is not set")


async def sample_calls():

    Total_profit = 0
    win_count = 0
    loss_count = 0
    wins = 0
    losts = 0
    stake = 1
    max_losts = 0
    loss_amount = 0
    net_total = 0

    api = DerivAPI(app_id=app_id)

    connection_established = await api.ping({'ping': 1})

    if connection_established['ping']:
        print(connection_established['ping'],"--------connection_established--------")

    active_symbols = await api.active_symbols({"active_symbols": "brief", "product_type": "basic"})

    authorize = await api.authorize(api_token)
    
    cached_active_symbols = await api.cache.active_symbols({"active_symbols": "brief", "product_type": "basic"})

    assets = await api.cache.asset_index({"asset_index": 1})

    execute = True

    while execute:

        
        # Forward propagation to get the output
        random_number = await main()

        starting_balance = await api.balance()

        proposal = await api.proposal({
            
            "proposal": 1,
            "amount": stake,
            "barrier": random_number,
            "basis": "stake",
            "contract_type": "DIGITDIFF",
            "currency": "USD",
            "duration": 2,
            "duration_unit": "t",
            "symbol": "R_25"
        })

        response = await api.buy({"buy": proposal.get('proposal').get('id'), "price": 5000})
        
        if response and response.get('buy') and response.get('buy').get('contract_id'):

            contract_id = response.get('buy').get('contract_id')
            
           
            # Assuming the contract ID is now correctly retrieved, proceed with the call
            poc = await api.proposal_open_contract({

                "proposal_open_contract": 1,
                "contract_id": contract_id
            })
            
            # Check if contract is closed and print profit/loss
            if poc and poc.get('proposal_open_contract'):

                current_spot = poc.get('proposal_open_contract').get('current_spot')

                barrier = poc.get('proposal_open_contract').get('barrier')

                contract_type = poc.get('proposal_open_contract').get('contract_type')

                await asyncio.sleep(5)

                ending_balance = await api.balance()

                # print(starting_balance.get('balance'))
                # print(ending_balance.get('balance'))

                profit = ending_balance.get('balance')['balance'] - starting_balance.get('balance')['balance'] 

                Total_profit = Total_profit + profit 

                if profit > 0 :

                    losts = 0

                    loss_amount = 0
                    
                    wins = wins + 1

                    win_count = win_count + 1

                    net_total = net_total + profit

                    stake = 1

                    print( "D : ",random_number,"  stake : ",stake, "  profit : ",profit," -------> Total_profit : ",Total_profit,"    net_profit : ",net_total,"    wins = ",win_count,"  losts = ",loss_count,"  max_losts : ",max_losts )  
                    print("\n")


                    

                else :
                    
                    wins = 0
                    
                    losts = losts + 1

                    loss_amount = loss_amount + stake 

                    if max_losts < losts :

                        max_losts = losts
                    
                    loss_count = loss_count + 1

                    net_total = net_total + profit

                    # MARTINGALE:

                    # if losts > 0 :

                    #      stake = loss_amount * 11

                    print( "D : ",random_number,"  stake : ",stake, "  profit : ",profit," -------> Total_profit : ",Total_profit,"    net_profit : ",net_total,"    wins = ",win_count,"  losts = ",loss_count,"  max_losts : ",max_losts )  
                    print("\n")

                         

            else:

                print("Buy order failed or contract ID not found in response.")

                     
        else:
             print("No response")

        
        if Total_profit >= 0.01 or Total_profit < 0 :
                
                Total_profit = 0

                print("\n###### DONE #######\n")

                await train()


asyncio.run(sample_calls())

