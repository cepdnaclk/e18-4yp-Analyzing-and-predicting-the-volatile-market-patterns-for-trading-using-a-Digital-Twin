import numpy as np
import random
import tensorflow as tf


class DeepQLearningRLAgent:
    def __init__(self,learning_rate=0.001, discount_factor=0.95, epsilon=1.0, epsilon_decay=0.995):
        self.model = self._build_model()
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        

    def _build_model(self):
        # Input = reward and number sequence
        # Output = prediction of the next number of this sequence

        model = tf.keras.Sequential([
            
            tf.keras.layers.Conv1D(filters=128, strides=2 , kernel_size=10, activation='selu' , kernel_regularizer=tf.keras.regularizers.L2(0.003),input_shape=(None, 1)),
            tf.keras.layers.Conv1D(filters=64, strides=2 , kernel_regularizer=tf.keras.regularizers.L2(0.003),kernel_size=5, activation='selu', padding='same'),
            tf.keras.layers.LSTM(units=64, kernel_regularizer=tf.keras.regularizers.L2(0.003) , return_sequences=True),
            tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.LSTM(units=50 , kernel_regularizer=tf.keras.regularizers.L2(0.003)),
            tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(10)  # Output layer 
        ])

        try :
            model.load_weights('my_model.keras')
        except :
            pass

        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(0.001))
        model.save('my_model.keras')
        
        return model

    def get_action(self, state):

        state = np.reshape(state, [1, -1])  # Reshape for the model
        if random.random() < self.epsilon:
            return random.randint(0, 9)  # Explore
        else:
            q_values = self.model.predict(state)[0]
            return np.argmax(q_values)  # Exploit

    def update(self, state, action,reward,next_state):
        """
        Updates the model based on the given experience (state, action, reward, next_state).

        Args:
            state (array-like): The current state of the environment.
            action (int): The action taken in the current state.
            reward (float): The reward received for taking the action.
            next_state (array-like): The next state reached after taking the action.
        """

        # Initialize target_q as a zero array with the same length as action_size
        target_q = np.zeros(10)

        action = int(action)  # Ensure action is an integer
        reward = int(reward)  # Ensure reward is a float

        state = np.reshape(state, [1, -1])
        next_state = np.reshape(next_state, [1, -1])


        # Calculate Q-values for the next state using the model:
        next_q_values = self.model.predict(next_state)[0]  # Assuming prediction returns a 1D array

        # Update target Q-value using Bellman equation:
        target_q[action] = reward + self.discount_factor * np.max(next_q_values)

        # Reshape target_q to a 2D array for fit:
        target_q = np.array([target_q])

        # Train the model with the experience (state, target_q):
        self.model.fit(state, target_q, epochs=1, verbose=0)


    def get_state(self, reward, number_sequence):
        
        # 3. Combine into a numerical state representation (consider normalization)
        state_vector = [
            reward,
            *number_sequence,
        ]

        return state_vector