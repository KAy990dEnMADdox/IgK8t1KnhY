# 代码生成时间: 2025-09-21 14:32:24
import pandas as pd
from sqlalchemy import create_engine, text

"""
This script demonstrates how to prevent SQL injection vulnerabilities
when interacting with a database using the pandas and sqlalchemy libraries.
"""

# Define the database connection parameters
DB_USERNAME = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'your_host'
DB_PORT = 'your_port'
DB_NAME = 'your_database'

# Create a secure database connection using SQLAlchemy
engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def fetch_data(query, params):
    """
    Fetch data from the database using a parameterized query to prevent SQL injection.
    
    :param query: The SQL query as a string with placeholders for parameters
    :param params: A dictionary of parameters to be used in the query
    :return: A pandas DataFrame containing the query results
    """
    try:
        # Use the pandas read_sql_query function with a parameterized query
        df = pd.read_sql_query(text(query), engine, params=params)
        return df
    except Exception as e:
        # Handle any exceptions that occur during database interaction
        print(f"An error occurred: {e}")
        return None

# Example usage of the fetch_data function
if __name__ == '__main__':
    # Define a sample query with placeholders
    query = "SELECT * FROM users WHERE user_id = :user_id AND email = :email"
    # Define the parameters for the query
    params = {"user_id": 1, "email": "example@example.com"}
    
    # Fetch data from the database
    result = fetch_data(query, params)
    
    # Print the result
    if result is not None:
        print(result)