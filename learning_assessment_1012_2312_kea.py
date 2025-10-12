# 代码生成时间: 2025-10-12 23:12:51
import pandas as pd

"""
Learning Assessment Program

This program evaluates the learning effectiveness of students based on their
scores in various subjects. It reads data from a CSV file, performs analysis,
and outputs the results."""

def load_data(file_path):
    """
    Loads data from a CSV file.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the student scores.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    pd.errors.EmptyDataError: If the file is empty.
    pd.errors.ParserError: If the file has parsing errors.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        raise
    except pd.errors.ParserError:
        print(f"Error: There was a parsing error in the file {file_path}.")
        raise


def analyze_scores(scores_df):
    """
    Analyzes the scores DataFrame.
    
    Args:
    scores_df (pd.DataFrame): The DataFrame containing student scores.
    
    Returns:
    dict: A dictionary with analysis results.
    """
    analysis_results = {}
    # Calculate mean scores for each subject
    for subject in scores_df.columns:
        if subject != 'Student':
            analysis_results[f'Mean {subject} Score'] = scores_df[subject].mean()
    
    # Calculate the number of students with scores above a certain threshold
    threshold = 70
    passing_students = 0
    for subject in scores_df.columns:
        if subject != 'Student':
            if (scores_df[subject] > threshold).sum() > 0:
                passing_students += 1
    
    analysis_results['Number of Students Passing'] = passing_students
    return analysis_results


def main():
    """
    Main function to run the learning assessment program.
    """
    file_path = 'student_scores.csv'  # Replace with the actual file path
    try:
        scores_df = load_data(file_path)
        analysis_results = analyze_scores(scores_df)
        print("Learning Assessment Results:
", analysis_results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()