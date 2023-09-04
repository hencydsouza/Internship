import pandas as pd
import string

class DataValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error reading CSV data: {e}")
            self.data = None

    def find_null_values(self):
        if self.data is not None:
            null_counts = self.data.isnull().sum()
            print("Null value counts:")
            print(null_counts)
        else:
            print("No data to check for null values.")

    def find_invalid_characters(self):
        if self.data is not None:
            invalid_characters = {}
            for column in self.data.columns:
                invalid_chars_count = 0
                for index, value in self.data[column].dropna().items():
                    if any(char not in string.printable for char in str(value)):
                        invalid_chars_count += 1
                if invalid_chars_count > 0:
                    invalid_characters[column] = invalid_chars_count
            if invalid_characters:
                print("Invalid character counts:")
                print(invalid_characters)
            else:
                print("No invalid characters found.")
        else:
            print("No data to check for invalid characters.")

validator = DataValidator('C:/Users/hency/OneDrive/Desktop/Internship/assignment/assignment1/data.csv')

validator.read_csv_data()

validator.find_null_values()

validator.find_invalid_characters()
