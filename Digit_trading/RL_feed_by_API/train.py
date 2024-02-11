
from my_game_env import MyGameEnv
from q_learning_agent import QLearningAgent
import pickle 
import asyncio
from last_digit_API import stream_last_digits

def save_agent(agent, filename):
    with open(filename, "wb") as f:
        pickle.dump(agent, f)

async def fetch_x_symbols(num_symbols):
    # Fetch X symbols from API (replace with your implementation)
    x_symbols = await asyncio.gather(*[stream_last_digits() for _ in range(num_symbols)])
    return x_symbols

# Training parameters
NUM_EPISODES = 1000
EPISODE_LENGTH = 10  # Length of each episode based on X symbols
EPSILON_DECAY = 0.999  # Rate of decay for exploration
MIN_EPSILON = 0.01  # Minimum exploration rate



async def train():

    # Create the environment
    env = MyGameEnv()

    # Create the agent
    agent = QLearningAgent(env)

    # Training loop
    for episode in range(NUM_EPISODES):

        # Fetch X symbols for the episode
        x_symbols = await fetch_x_symbols(EPISODE_LENGTH)

        state = env.reset(x_symbols)
        done = False

        # Initialize epsilon for each episode
        epsilon = 1.0  # Start with full exploration

        while not done:
            # Explore or exploit based on epsilon-greedy strategy
            action = agent.choose_action(state)

            # Step in the environment
            next_state, reward, done, _ = env.step(action)

            # Update Q-table (no experience storage needed for tabular Q-learning)
            agent.learn(state, action, reward, next_state)

            state = next_state

            # Adapt exploration after each step
            epsilon = max(MIN_EPSILON, epsilon * EPSILON_DECAY)


            print(f"Episode {episode+1}: Epsilon: {epsilon}, Reward: {reward}")

    save_agent(agent, "trained_agent.pkl")  # Replace with your saving method

    # Close the environment
    env.close()

asyncio.run(train())