from my_game_env import MyGameEnv
from q_learning_agent import QLearningAgent
import random
import asyncio
import pickle
from last_digit_API import stream_last_digits

global total_reward

# Game parameters

REWARD_WIN = 0.99
REWARD_LOSS = -10
EPSILON_DECAY = 0.999  # Rate of decay for exploration
MIN_EPSILON = 0.01  # Minimum exploration rate


# Initialize environment and agent
env = MyGameEnv()

# Load the trained agent
agent = pickle.load(open("trained_agent.pkl", "rb"))   #open in binary mode
             

async def main():
    
    total_reward = 0
    wins = 0
    losts = 0
    runs = 0
    pre_x_symbol = await stream_last_digits()
    
    while True:
            
            runs += 1
            
            # Get D suggestion from agent

            d_symbol = agent.choose_action(pre_x_symbol)
            print("D: ",d_symbol)

            await asyncio.sleep(2)

            x_symbol = await stream_last_digits()

            # Calculate reward based on imaginary opponent's logic (replace with your logic)
            reward = REWARD_WIN if x_symbol != d_symbol else REWARD_LOSS

            if reward == REWARD_WIN :
                 wins += 1
            else :
                 losts += 1
            
            total_reward += reward

            print("D: ",d_symbol,"   X: ",x_symbol,"  profit: ",reward,"Total profit: ",total_reward,"  wins: ",wins," losts: ",losts," runs: ",runs,"\n")

            pre_x_symbol = x_symbol

            done = False
            # Initialize epsilon for each episode
            epsilon = 1.0  # Start with full exploration

            while not done:
                
                # Step in the environment
                next_state, reward, done, _ = env.step(d_symbol)

                # Update Q-table (no experience storage needed for tabular Q-learning)
                agent.learn(x_symbol, d_symbol, reward, next_state)

                x_symbol = next_state

                # Adapt exploration after each step
                epsilon = max(MIN_EPSILON, epsilon * EPSILON_DECAY)

            

if __name__ == "__main__":
    asyncio.run(main())