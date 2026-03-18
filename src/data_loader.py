import pandas as pd
from pathlib import Path

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    required_columns = {"date", "product", "price", "quantity", "stock"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Missing required columns")

    return df