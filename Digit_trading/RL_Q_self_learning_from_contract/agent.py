import numpy as np
import random

class RandomNumberRLAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay=0.995):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def get_action(self, state):
        if random.random() < self.exploration_rate:
            return random.randint(0, 9)  # Explore
        else:
            return np.argmax(self.q_table.get(state, [0] * 10))  # Exploit

    def update(self, state, action, reward, next_state):
        action = int(action)
        old_q_value = self.q_table.get(state, [0] * 10)[action]
        next_max_q = max(self.q_table.get(next_state, [0] * 10))
        new_q_value = old_q_value + self.learning_rate * (reward + self.discount_factor * next_max_q - old_q_value)

        self.q_table.setdefault(state, [0] * 10)
        self.q_table[state][action] = new_q_value
        self.exploration_rate *= self.exploration_decay

    def get_state(self, net_total, past_numbers, past_profits):
            # 1. Discretize net_total (e.g., buckets of 0.5 profit range)
            net_total_bucket = max(0, int(net_total // 0.5)) 

            # 2. Represent past numbers/profits (consider how many are relevant)
            recent_history = past_numbers[-3:] + past_profits[-3:]

            # 3. Combine into a state representation 
            return str(net_total_bucket) + "_" + "_".join(map(str, recent_history))