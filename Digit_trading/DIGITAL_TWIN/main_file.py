from Contract_sending import sample_calls  
from last_digit_API import stream_last_digits
import tensorflow as tf
import numpy as np
import pandas as pd

def sum_to_index(arr, i):
  sum = 0
  for j in range(i + 1):  # Include the element at the i-th index
    sum += arr[j]
  return sum

async def run() :

    model_test = tf.keras.models.load_model('my_model.keras')

    app_id = 52956
    api_token = 'BkZ6gvARgNCQd3h'

    real_trade_starting_point = 40   # margin of real trade starts
    possible_real_points = 40        # 25 for 95 dollar capital (max 51 for 2105 dollars capital)
    stopping_profit = 30            # trade stop point while another outlier comes

    c = 0
    actual_consequent = 0
    p = 0
    Tp = 0
    ml = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,5,5,6,7,8,9,10,11,12,14,16,18,20,22,25,28,32,36,40,45,50,57,64,72,81,91,103,116,130,146,165,185,208,234]
    RT1 = False
    RT2 = False
    Rc = 0
    seeking_outlier = 80

    digit_array = []

    while True :

        for k in range(11):
            if k <=9:
                last_digit = await stream_last_digits()
                digit_array.append(int(last_digit))
                print(digit_array)

        array_1d = np.array(digit_array)
        array_2d = array_1d.reshape(1, 10)

        df = pd.DataFrame(array_2d)
        pre = model_test.predict(df)
        predictions = np.argmax(pre , axis = 1)
        print(predictions[0])

        profit = await sample_calls(predictions[0],ml[Rc],app_id,api_token)

        with open("sequences.csv", 'a', newline='') as f:  
            f.write(f"{digit_array}\n")
        
        if profit > 0 :
            with open("Normal_wins.csv", 'a', newline='') as f:  
                f.write(f"consequent : {actual_consequent}\n")
            actual_consequent = 0
        else :
            actual_consequent += 1

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
                with open("REAL_wins.csv", 'a', newline='') as f:  
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
                    with open("REAL_wins.csv", 'a', newline='') as f:  
                        f.write(f"!!!!!!!!!!!!!!!!!!!!!!!!!!! Profit : {Tp} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

        if RT1 and c == real_trade_starting_point :
            RT2 = True
        
        digit_array = []
        print('Total profit : ',Tp)
