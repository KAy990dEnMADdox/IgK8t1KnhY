# 代码生成时间: 2025-09-19 16:22:04
import os
import pandas as pd
from pathlib import Path

"""
Batch File Renamer Tool
This tool allows for the batch renaming of files in a specified directory.
It uses a pandas DataFrame to manage the mapping between old and new names.
"""

class BatchFileRenamer:
    def __init__(self, directory):
        """
        Initializes the BatchFileRenamer instance with the target directory.
        :param directory: The path to the directory containing files to be renamed.
        """
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f"The directory {self.directory} does not exist.")

    def get_existing_files(self):
        """
        Retrieves a list of files in the directory.
        :return: A list of file names.
        """
        return [file.name for file in self.directory.iterdir() if file.is_file()]

    def load_mapping(self, mapping_file):
        """
        Loads the mapping from a CSV file.
        :param mapping_file: Path to the CSV file containing old and new file names.
        """
        try:
            df = pd.read_csv(mapping_file)
            if 'old_name' not in df.columns or 'new_name' not in df.columns:
                raise ValueError("The mapping file must contain 'old_name' and 'new_name' columns.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The mapping file {mapping_file} does not exist.")
        except pd.errors.EmptyDataError:
            raise ValueError("The mapping file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the mapping file: {e}")

    def rename_files(self, mapping_df):
        """
        Renames the files based on the provided mapping DataFrame.
        :param mapping_df: DataFrame with 'old_name' and 'new_name' columns.
        """
        for index, row in mapping_df.iterrows():
            old_name = row['old_name']
            new_name = row['new_name']
            old_path = self.directory / old_name
            if old_path.exists():
                new_path = self.directory / new_name
                new_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the new directory exists
                os.rename(old_path, new_path)
                print(f"Renamed '{old_name}' to '{new_name}'")
            else:
                print(f"File '{old_name}' not found. Skipping...")

    def run(self, mapping_file):
        """
        Runs the batch file renamer.
        :param mapping_file: Path to the CSV file with rename mappings.
        """
        mapping_df = self.load_mapping(mapping_file)
        self.rename_files(mapping_df)

# Usage example
if __name__ == '__main__':
    try:
        directory = 'path/to/your/directory'
        mapping_file = 'path/to/your/mapping.csv'
        renamer = BatchFileRenamer(directory)
        renamer.run(mapping_file)
    except Exception as e:
        print(f"An error occurred: {e}")