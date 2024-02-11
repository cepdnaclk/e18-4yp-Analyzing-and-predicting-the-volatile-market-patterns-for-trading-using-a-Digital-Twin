           
import asyncio

global wining_differlist,wining_matchlist,wining_overlist,wining_underlist

global loosing_differlist,loosing_matchlist,loosing_overlist,loosing_underlist

global even,odd
 

wining_differlist  = [0,0,0,0,0,0,0,0,0,0]
wining_matchlist   = [0,0,0,0,0,0,0,0,0,0]
wining_overlist    = [0,0,0,0,0,0,0,0,0,0]
wining_underlist   = [0,0,0,0,0,0,0,0,0,0]


probability_differlist = [0,0,0,0,0,0,0,0,0,0]
probability_matchlist  = [0,0,0,0,0,0,0,0,0,0]
probability_overlist   = [0,0,0,0,0,0,0,0,0,0]
probability_underlist  = [0,0,0,0,0,0,0,0,0,0]

even = 0

odd = 0

async def process_digits(last_digit,runs):
        
        async def digit_is_0():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 0 :
                                element = element + 1
                                wining_matchlist[index] = element 

            for index,element in enumerate(wining_differlist):
                            if index != 0 :
                                element = element + 1 
                                wining_differlist[index] = element

            for index,element in enumerate(wining_underlist) :
                            if index != 0 :
                                element = element + 1 
                                wining_underlist[index] = element
                    
            # even = even + 1

        async def digit_is_1():

            #for winnings
            for index,element in enumerate(wining_matchlist):
                            if index == 1 :
                                element = element + 1
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 1 :
                                element = element + 1
                                wining_differlist[index] = element
                                 
                    
            for index,element in enumerate(wining_underlist) :
                            if index != 0 and index != 1 :
                                element = element + 1
                                wining_underlist[index] = element 

            for index,element in enumerate(wining_overlist):
                            if index == 0 :
                                element = element + 1 
                                wining_overlist[index] = element
                    
            # odd = odd + 1

        async def digit_is_2():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 2 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 2 :
                                element = element + 1 
                                wining_differlist[index] = element
                    
            for index,element in enumerate(wining_underlist) :
                            if index != 0 and index != 1 and index != 2 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index == 0 or index == 1 :
                                element = element + 1
                                wining_overlist[index] = element 
                    
            # even = even + 1


        async def digit_is_3():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 3 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 3 :
                                element = element + 1 
                                wining_differlist[index] = element
                    
            for index,element in enumerate(wining_underlist) :
                            if index != 0 and index != 1 and index != 2 and  index != 3 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index == 0 or index == 1 or index == 2 :
                                element = element + 1
                                wining_overlist[index] = element 
                    
            # odd = odd + 1


        async def digit_is_4():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 4 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 4 :
                                element = element + 1
                                wining_differlist[index] = element 
                    
            for index,element in enumerate(wining_underlist) :
                             if index == 5 or index == 6 or index == 7 or index == 8 or index == 9 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index == 0 or index == 1 or index == 2 or index == 3 :
                                element = element + 1 
                                wining_overlist[index] = element
                    
            # even = even + 1


        async def digit_is_5():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 5 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 5 :
                                element = element + 1
                                wining_differlist[index] = element 
                    
            for index,element in enumerate(wining_underlist) :
                            if index == 6 or index == 7 or index == 8 or index == 9 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index == 0 or index == 1 or index == 2 or index == 3 or index == 4 :
                                element = element + 1
                                wining_overlist[index] = element 
                    
            # odd = odd + 1

            

        async def digit_is_6():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 6 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 6 :
                                element = element + 1 
                                wining_differlist[index] = element
                    
            for index,element in enumerate(wining_underlist) :
                            if index == 7 or index == 8 or index == 9 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index != 6 and index != 7 and index != 8 and index != 9 :
                                element = element + 1 
                                wining_overlist[index] = element
                    
            # even = even + 1

            

        async def digit_is_7():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 7 :
                                element = element + 1
                                wining_matchlist[index] = element 

            for index,element in enumerate(wining_differlist):
                            if index != 7 :
                                element = element + 1
                                wining_differlist[index] = element 
                    
            for index,element in enumerate(wining_underlist) :
                            if index == 8 or index == 9 :
                                element = element + 1
                                wining_underlist[index] = element 

            for index,element in enumerate(wining_overlist):
                            if index != 7 and index != 8 and index != 9 :
                                element = element + 1
                                wining_overlist[index] = element 
                    
            # odd = odd + 1

            

        async def digit_is_8():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 8 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 8 :
                                element = element + 1
                                wining_differlist[index] = element 
                    
            for index,element in enumerate(wining_underlist) :
                            if index == 9 :
                                element = element + 1 
                                wining_underlist[index] = element

            for index,element in enumerate(wining_overlist):
                            if index != 8 and index != 9 :
                                element = element + 1 
                                wining_overlist[index] = element
                    
            # even = even + 1


        async def digit_is_9():

            #for winnings

            for index,element in enumerate(wining_matchlist):
                            if index == 9 :
                                element = element + 1 
                                wining_matchlist[index] = element

            for index,element in enumerate(wining_differlist):
                            if index != 9 :
                                element = element + 1 
                                wining_differlist[index] = element
                    
            for index,element in enumerate(wining_overlist) :
                            if index != 9 :
                                element = element + 1 
                                wining_overlist[index] = element
                    
            # odd = odd + 1

            
        
        # print("Received last digit:", last_digit )

        if last_digit == '0' :
                await digit_is_0()
       
        if last_digit == '1' :
                await digit_is_1()

        if last_digit == '2' :
                await digit_is_2()
        
        if last_digit == '3' :
                await digit_is_3()
        
        if last_digit == '4' :
                await digit_is_4()
        
        if last_digit == '5' :
                await digit_is_5()

        if last_digit == '6' :
                await digit_is_6()
        
        if last_digit == '7' :
                await digit_is_7()

        if last_digit == '8' :
                await digit_is_8()
        
        if last_digit == '9' :
                await digit_is_9()

        
        for index,element in enumerate(wining_matchlist) :
                element = element / runs
                probability_matchlist[index] = element
        
        for index,element in enumerate(wining_differlist) :
                element = element / runs
                probability_differlist[index] = element
        
        for index,element in enumerate(wining_overlist) :
                element = element / runs
                probability_overlist[index] = element
        
        for index,element in enumerate(wining_underlist) :
                element = element / runs
                probability_underlist[index] = element
        print("  ------        Average probability of each option wins         -------\n")
        
        print("digits            0     1     2    3      4      5     6     7     8    9           counts of wining each options\n")
                
        formatted_numbers = [f"{num:.1f}" for num in probability_matchlist ]  # Format numbers using list comprehension
        print("match       : [ "," , ".join(formatted_numbers)," ]        ",wining_matchlist,"\n")  # Join with spaces and print        

     
        formatted_numbers = [f"{num:.1f}" for num in probability_differlist]  # Format numbers using list comprehension
        print("differ      : [ "," , ".join(formatted_numbers)," ]        ",wining_differlist,"\n")  # Join with spaces and print
       
      
        formatted_numbers = [f"{num:.1f}" for num in probability_overlist]  # Format numbers using list comprehension
        print("over_digit  : [ "," , ".join(formatted_numbers)," ]        ",wining_overlist,"\n")  # Join with spaces and print
        

        formatted_numbers = [f"{num:.1f}" for num in probability_underlist]  # Format numbers using list comprehension
        print("under_digit : [ "," , ".join(formatted_numbers)," ]        ",wining_underlist,"\n")  # Join with spaces and print
         

           
