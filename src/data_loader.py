import pandas as pd
from pathlib import Path

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    required_columns = {"date", "product", "price", "quantity", "stock"}
    if df.isnull().sum().any():
        raise ValueError("Dataset contains missing values")

    return df