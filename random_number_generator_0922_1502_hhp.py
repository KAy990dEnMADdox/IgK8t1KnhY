# 代码生成时间: 2025-09-22 15:02:31
import pandas as pd
import numpy as np

"""
Random Number Generator

This module generates random numbers using pandas and numpy.
It includes error handling, documentation, and follows Python best practices.
"""

class RandomNumberGenerator:
    """
    A class to generate random numbers with pandas and numpy.
    """
    
    def __init__(self, min_value, max_value, num_samples):
        """
        Initialize the RandomNumberGenerator with min_value, max_value, and num_samples.
        
        Parameters:
        min_value (int): The minimum value of the random numbers.
        max_value (int): The maximum value of the random numbers.
        num_samples (int): The number of random samples to generate.
        """
        self.min_value = min_value
        self.max_value = max_value
        self.num_samples = num_samples
        self.random_numbers = []
        
        # Validate the input parameters
        if self.min_value >= self.max_value:
            raise ValueError("Min value must be less than max value")
        if self.num_samples <= 0:
            raise ValueError("Num samples must be greater than 0")
        
    def generate(self):
        """
        Generate random numbers using numpy.
        """
        try:
            self.random_numbers = np.random.randint(self.min_value, self.max_value+1, self.num_samples).tolist()
            return self.random_numbers
        except Exception as e:
            print(f"Error generating random numbers: {e}")
            
    def to_dataframe(self):
        """
        Convert the random numbers to a pandas dataframe.
        """
        try:
            df = pd.DataFrame(self.random_numbers, columns=["Random Numbers"])
            return df
        except Exception as e:
            print(f"Error converting to dataframe: {e}")
            
# Example usage
if __name__ == "__main__":
    rng = RandomNumberGenerator(1, 100, 10)
    random_numbers = rng.generate()
    print("Random Numbers: ", random_numbers)
    df = rng.to_dataframe()
    print(df)
