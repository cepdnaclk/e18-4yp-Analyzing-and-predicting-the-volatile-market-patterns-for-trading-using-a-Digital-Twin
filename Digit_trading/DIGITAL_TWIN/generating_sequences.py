import pandas as pd
import numpy as np

def generate_sequences(N, n):
    """
    Generates N sequences of integers (0-9 range) of size n as NumPy arrays, 
    along with their corresponding (n+1)th numbers.
    """

    x_values = np.empty((N, n), dtype=int)  # Initialize empty array for sequences
    y_values = np.zeros(N, dtype=int)       # Initialize empty array for (n+1)th numbers

    for i in range(N):  
        sequence = np.random.randint(0, 10, size=n)  # Generate NumPy sequence
        next_number = np.random.randint(0, 10)

        x_values[i] = sequence
        y_values[i] = next_number

    # Create DataFrames and save to CSV
    df_x = pd.DataFrame(x_values)  # DataFrame can be created directly from NumPy array
    df_x.to_csv('x_values.csv', index=False, header=False) 

    df_y = pd.DataFrame({'y_value': y_values})
    df_y.to_csv('y_values.csv', index=False)

# Example usage:
N = 1000  # Number of sequences
n = 11  # Length of each sequence
generate_sequences(N, n)