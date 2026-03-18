import pandas as pd

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if df["date"].isnull().any():
        raise ValueError("Invalid date values found in dataset")

    df["revenue"] = df["price"] * df["quantity"]
    df["month"] = df["date"].dt.to_period("M")

    return df