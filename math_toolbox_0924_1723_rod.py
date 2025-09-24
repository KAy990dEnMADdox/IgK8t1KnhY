# 代码生成时间: 2025-09-24 17:23:49
import pandas as pd

"""
**Math Toolbox**
A collection of mathematical calculation tools using Python and Pandas.

Attributes:
    None

Methods:
    calculate_sum(data): Calculate the sum of a given DataFrame or Series.
    calculate_mean(data): Calculate the mean of a given DataFrame or Series.
    calculate_median(data): Calculate the median of a given DataFrame or Series.
    calculate_max(data): Calculate the maximum value in a given DataFrame or Series.
    calculate_min(data): Calculate the minimum value in a given DataFrame or Series."""

class MathToolbox:
    def __init__(self):
        """Initialize the MathToolbox class."""
        pass

    def calculate_sum(self, data):
        """Calculate the sum of a given DataFrame or Series.

        Args:
            data (pd.DataFrame or pd.Series): The input data.

        Returns:
            float or int: The sum of the data or None if the input is invalid.

        Raises:
            TypeError: If the input data is not a DataFrame or Series.
        """
        if isinstance(data, (pd.DataFrame, pd.Series)):
            return data.sum()
        else:
            raise TypeError("Input data must be a DataFrame or Series.")

    def calculate_mean(self, data):
        """Calculate the mean of a given DataFrame or Series.

        Args:
            data (pd.DataFrame or pd.Series): The input data.

        Returns:
            float or int: The mean of the data or None if the input is invalid.

        Raises:
            TypeError: If the input data is not a DataFrame or Series.
        """
        if isinstance(data, (pd.DataFrame, pd.Series)):
            return data.mean()
        else:
            raise TypeError("Input data must be a DataFrame or Series.")

    def calculate_median(self, data):
        """Calculate the median of a given DataFrame or Series.

        Args:
            data (pd.DataFrame or pd.Series): The input data.

        Returns:
            float or int: The median of the data or None if the input is invalid.

        Raises:
            TypeError: If the input data is not a DataFrame or Series.
        """
        if isinstance(data, (pd.DataFrame, pd.Series)):
            return data.median()
        else:
            raise TypeError("Input data must be a DataFrame or Series.")

    def calculate_max(self, data):
        """Calculate the maximum value in a given DataFrame or Series.

        Args:
            data (pd.DataFrame or pd.Series): The input data.

        Returns:
            float or int: The maximum value in the data or None if the input is invalid.

        Raises:
            TypeError: If the input data is not a DataFrame or Series.
        """
        if isinstance(data, (pd.DataFrame, pd.Series)):
            return data.max()
        else:
            raise TypeError("Input data must be a DataFrame or Series.")

    def calculate_min(self, data):
        """Calculate the minimum value in a given DataFrame or Series.

        Args:
            data (pd.DataFrame or pd.Series): The input data.

        Returns:
            float or int: The minimum value in the data or None if the input is invalid.

        Raises:
            TypeError: If the input data is not a DataFrame or Series.
        """
        if isinstance(data, (pd.DataFrame, pd.Series)):
            return data.min()
        else:
            raise TypeError("Input data must be a DataFrame or Series.")

# Example usage:
if __name__ == "__main__":
    toolbox = MathToolbox()
    data = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50]
    })

    print("Sum: ", toolbox.calculate_sum(data))
    print("Mean: ", toolbox.calculate_mean(data))
    print("Median: ", toolbox.calculate_median(data))
    print("Max: ", toolbox.calculate_max(data))
    print("Min: ", toolbox.calculate_min(data))
