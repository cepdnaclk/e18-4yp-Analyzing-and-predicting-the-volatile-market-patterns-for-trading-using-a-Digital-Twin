import numpy as np

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.95, epsilon=1.0):
        self.env = env
        self.action_size = env.action_space.n
        self.Q = np.zeros((env.observation_space.n, self.action_size))# Q-table
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon  # Exploration rate

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            # Explore (random action)
            return self.env.action_space.sample()
        else:
            # Exploit (best action based on Q-values)
            return np.argmax(self.Q[state])

    def store_experience(self, state, action, reward, next_state):
        # No experience storage for Q-learning with tabular representation
        pass

    def learn(self, state, action, reward, next_state=None):
        if next_state is None:  # Handle game ending after each interaction
            next_best_action = None
            target = reward
        else:
            next_best_action = np.argmax(self.Q[next_state])
            target = reward + self.discount_factor * self.Q[next_state, next_best_action]

            # Update Q-value
            self.Q[state, action] += self.learning_rate * (target - self.Q[state, action])

            