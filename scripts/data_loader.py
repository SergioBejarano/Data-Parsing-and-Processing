import pandas as pd

def load_employee_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame with the loaded data.
    """
    return pd.read_csv(file_path)