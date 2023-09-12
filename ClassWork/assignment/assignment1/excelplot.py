import pandas as pd
import matplotlib.pyplot as plt

class DataPlotter:
    def __init__(self, file_path):
        self.file_path = 'C:/Users/hency/OneDrive/Desktop/Internship/assignment/assignment1/data.xlsx'

    def read_excel_data(self):
        try:
            self.data = pd.read_excel(self.file_path)
        except Exception as e:
            print(f"Error reading Excel data: {e}")
            self.data = None

    def plot_linear(self, x_col, y_col):
        if self.data is not None:
            x_axis = self.data['X values']
            y_axis = self.data['Y values']
            plt.bar(x_axis, y_axis, width=5)
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.show()
        else:
            print("No data to plot.")

plotter = DataPlotter('data.xlsx')

plotter.read_excel_data()

if plotter.data is not None:
    plotter.plot_linear('X', 'Y')
