from my_game_env import MyGameEnv
from q_learning_agent import QLearningAgent
import random
import asyncio
import pickle
from last_digit_API import stream_last_digits

def save_agent(agent, filename):
    with open(filename, "wb") as f:
        pickle.dump(agent, f)

global total_reward

# Game parameters

REWARD_WIN = 0.99
REWARD_LOSS = -10
EPSILON_DECAY = 0.999  # Rate of decay for exploration
MIN_EPSILON = 0.01  # Minimum exploration rate


# Initialize environment and agent
env = MyGameEnv()

async def main():
     
    while True:
            
            x_symbol = await stream_last_digits()
            
            # Load the trained agent
            agent = pickle.load(open("trained_agent.pkl", "rb"))   #open in binary mode
            
            # Get D suggestion from agent

            d_symbol = agent.choose_action(x_symbol)
            print("D: ",d_symbol)

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
           
            return d_symbol
            

            
asyncio.run(main())