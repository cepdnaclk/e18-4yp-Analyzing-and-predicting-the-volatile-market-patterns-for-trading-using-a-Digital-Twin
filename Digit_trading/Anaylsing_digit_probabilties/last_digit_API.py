import websockets
import asyncio
import json
import math

from Probability_Distributions import process_digits 


app_id = 52537  # Replace with your app_id

ws_url = f"wss://ws.derivws.com/websockets/v3?app_id={app_id}"

async def stream_last_digits():

    global runs

    runs =0

    async with websockets.connect(ws_url) as ws:

        print("Connected to Deriv API")

        subscribe_request = {"subscribe": 1, "ticks": "R_100"}

        await ws.send(json.dumps(subscribe_request))

        while True:

            runs += 1

            try:
                # await asyncio.sleep(4)

                data = await asyncio.wait_for(ws.recv(), timeout=5)

                message = json.loads(data)

                if message.get("error"):

                    print(f"Error: {message['error']['message']}")

                elif message.get("tick"):

                    tick = message["tick"]

                    if len(str(tick["quote"])) == 7 :
                       
                       last_digit = str(tick["quote"])[-1] 

                    else :

                        last_digit = str(0)
                        

                    await process_digits(last_digit,runs)

                    print ("tick :  = ",tick["quote"] ,"\n")

                    print ("last_digit :  = ",last_digit,"\n")

                    print ("number of ticks received = ",runs,"\n")
                    
            except asyncio.TimeoutError:

                print("WebSocket timed out. Reconnecting...")

                await stream_last_digits()  # Reconnect on timeout

            except websockets.ConnectionClosed:

                print("WebSocket connection closed.")

                break


asyncio.run(stream_last_digits())

