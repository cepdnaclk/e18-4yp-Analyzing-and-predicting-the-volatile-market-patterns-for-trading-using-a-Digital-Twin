import csv



def sum_to_index(arr, i):
  sum = 0
  for j in range(i + 1):  # Include the element at the i-th index
    sum += arr[j]
  return sum


possible_real_points = 40
seeking_outlier = 65
real_trade_starting_point = 25
stopping_profit = 30
real_trade_on = False
seeking_outlier_found_and_next_trade = False
saved_instance = 0
count = 0
Total_profit = 0
Tp = 0

ml = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,5,5,6,7,8,9,10,11,12,14,16,18,20,22,25,28,32,36,40,45,50,57,64,72,81,91,103,116,130,146,165,185,208,234]


with open('Demo_Wins.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for consequent in csv_reader:
        print(len(consequent[0]))
        consequent = int(consequent[0])
        print(consequent)
        count += 1
        if consequent >= seeking_outlier and not(real_trade_on):
           real_trade_on = True
           saved_instance = count
        if saved_instance != count and real_trade_on and  consequent > real_trade_starting_point :
            real_consequent = consequent - real_trade_starting_point
            if real_consequent != 0  and real_consequent < possible_real_points:
                Total_profit +=  ml[real_consequent]*8 - sum_to_index(ml, real_consequent - 1)
                Tp +=  ml[real_consequent]*8 - sum_to_index(ml, real_consequent - 1)
                saved_instance = 0
            elif real_consequent == 0 : 
                Total_profit +=  ml[real_consequent]*8
                Tp +=  ml[real_consequent]*8
                saved_instance = 0
            elif real_consequent >= possible_real_points :
                Total_profit = Total_profit - sum_to_index(ml, possible_real_points-1)
                Tp = Total_profit - sum_to_index(ml, possible_real_points-1)


                print("--------------------capital wash-----------------------")

                with open("profit.csv", 'a', newline='') as f:  
                    f.write(f"--------------------capital wash-----------------------\n")
            
            if Tp >= stopping_profit :
                Tp = 0
                real_trade_on = False

            with open("profit.csv", 'a', newline='') as f:  
                    f.write(f"Profit : {Total_profit}\n")