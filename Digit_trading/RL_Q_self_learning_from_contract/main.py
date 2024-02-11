from Contract_sending import sample_calls  # Assuming your API logic is in this file
from agent import RandomNumberRLAgent
import asyncio
import pickle

global net_total,past_numbers,past_profits,wins,losts,consequent_losts,pre_consequent_losts,Total_profit

def save_agent(agent, filename):
    with open(filename, "wb") as f:
        pickle.dump(agent, f)


async def main():

    wins = 0
    losts = 0
    consequent_losts = 0
    pre_consequent_losts = 0
    Total_profit = 0

    net_total = 0
    past_numbers = []
    past_profits = []

    agent = pickle.load(open("trained_agent.pkl", "rb"))

    for episode in range(1000):

        state = agent.get_state(Total_profit, past_numbers, past_profits)
        random_number = agent.get_action(state)

        # Call the Deriv API for real
        try:
            random_number, profit, net_total = await sample_calls(random_number)  
        except Exception as e:
            print(f"Error during API call: {e}")
            profit = -1  # Simulate a loss on errors

        past_numbers.append(random_number)
        past_profits.append(profit)
        
        Total_profit += profit
        next_state = agent.get_state(Total_profit, past_numbers, past_profits)
        agent.update(state, random_number, profit, next_state)

        if profit > 0 :

            wins += 1
            consequent_losts = 0

        else  :

            losts += 1
            consequent_losts += 1

            if consequent_losts > pre_consequent_losts :

                pre_consequent_losts = consequent_losts  

         

        print(f"Episode: {episode}, Profit: {profit}, Net Total: {Total_profit}, Wins: {wins}, Losts: {losts}, consequent_losts: {pre_consequent_losts}")
        print("\n")
    
    save_agent(agent, "trained_agent.pkl") 

asyncio.run(main())
