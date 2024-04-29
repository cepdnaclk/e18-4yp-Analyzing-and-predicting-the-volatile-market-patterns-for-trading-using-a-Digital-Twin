from Contract_sending import sample_calls  
from last_digit_API import stream_last_digits
from RL_Agent import DeepQLearningRLAgent
import asyncio

def sum_to_index(arr, i):
  sum = 0
  for j in range(i + 1):  # Include the element at the i-th index
    sum += arr[j]
  return sum

async def run() :

    agent = DeepQLearningRLAgent()

    real_trade_starting_point = 25   # margin of real trade starts
    possible_real_points = 40        # 25 for 95 dollar capital (max 51 for 2105 dollars capital)
    stopping_profit = 30             # trade stop point while another outlier comes
    seeking_outlier = 65             #catching Outlier

    c = 0
    actual_consequent = 0
    p = 0
    Tp = 0
    ml = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,5,5,6,7,8,9,10,11,12,14,16,18,20,22,25,28,32,36,40,45,50,57,64,72,81,91,103,116,130,146,165,185,208,234]
    RT1 = False
    RT2 = False
    Rc = 0

    digit_array = []
    reward = 0

    while True :

        for k in range(11):
            if k <=9:
                last_digit = await stream_last_digits()
                digit_array.append(int(last_digit))
                print(digit_array)

        state = agent.get_state(reward, digit_array)
        predicted_number = agent.get_action(state)

        print("DIGITAL TWIN IS RUNNING................")
             

        if (RT2) :
            #REAL ACOUNT
            print("REAL TRADING IS STARTED................")
            app_id = 52956
            api_token = 'BkZ6gvARgNCQd3h'
        else :
            #DEMO ACOUNT
            print("DEMO TRADING IS STARTED................")
            app_id = 52956
            api_token = 'BkZ6gvARgNCQd3h'

        profit = await sample_calls(predicted_number,ml[Rc],app_id,api_token)

        with open("sequences.csv", 'a', newline='') as f:  
            f.write(f"{digit_array}\n")
        
        if profit > 0 :
            with open("DEMO_wins-REAL TIME.csv", 'a', newline='') as f:  
                f.write(f"{actual_consequent}\n")
            actual_consequent = 0
            reward = 8
        else :
            actual_consequent += 1
            reward = -1

        if not(RT2) :
            if profit > 0 :
                if c >= seeking_outlier :
                    RT1 = True
                c=0
            else  :
                c += 1         
        elif RT2 :
            if (profit > 0) and Rc < possible_real_points - 1 :
                p += ml[Rc+1]*8 - sum_to_index(ml, Rc)
                Tp += ml[Rc+1]*8 - sum_to_index(ml, Rc)
                with open("REAL_Wins-REAL TIME.csv", 'a', newline='') as f:  
                    f.write(f"consequent : {Rc} , Profit : {Tp}\n")
                Rc=0

                if p // stopping_profit == 1 :
                    RT1 = False
                    RT2 = False
                    p = 0
                    Rc=0
                    c = 0
            else  :
                Rc += 1
                if Rc == possible_real_points :
                    RT1 = False
                    RT2 = False
                    p = 0
                    Rc=0
                    c = 0
                    Tp = Tp - sum_to_index(ml,(possible_real_points - 1))
                    with open("REAL_wins-REAL TIME.csv", 'a', newline='') as f:  
                        f.write(f"!!!!!!!!!!!!!!!!!!!!!!!!!!! Profit : {Tp} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

        if RT1 and c == real_trade_starting_point :
            RT2 = True

        next_state = agent.get_state(reward, digit_array)
        agent.update(state, predicted_number,reward,next_state)

        digit_array = []
        print('Total profit : ',Tp)

asyncio.run(run())