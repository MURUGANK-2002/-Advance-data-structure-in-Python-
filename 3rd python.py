import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path):
    """Load dataset from a CSV or Excel file"""
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
    except Exception as e:
        print(f"Error loading dataset: {e}")

def display_summary_statistics(data):
    """Display summary statistics of the dataset"""
    print("\nSummary Statistics:")
    print(data.describe())

def visualize_data(data):
    """Generate visualizations for the dataset"""
    print("\nAvailable Columns:", data.columns.tolist())
    while True:
        choice = input("\nChoose Visualization: 1. Histogram 2. Exit: ")
        if choice == '1':
            col = input("Column for histogram: ")
            if col in data.columns:
                data[col].plot(kind='hist', title=f"Histogram of {col}", bins=20)
                plt.xlabel(col)
                plt.show()
            else:
                print("Invalid column name.")
        elif choice == '2':
            print("Exiting visualization menu.")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    file_path = input("Enter dataset path (CSV/Excel): ")
    data = load_dataset(file_path)
    if data is not None:
        print("\nDataset Loaded Successfully!\nFirst 5 Rows:\n", data.head())
        while True:
            choice = input("\nMain Menu: 1. Summary Statistics 2. Visualize Data 3. Exit: ")
            if choice == '1':
                display_summary_statistics(data)
            elif choice == '2':
                visualize_data(data)
            elif choice == '3':
                print("Exiting..")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
