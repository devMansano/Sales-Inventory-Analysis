import pandas as pd

LOW_STOCK_THRESHOLD = 10

def calculate_metrics(df: pd.DataFrame) -> dict:
    return {
        "total_revenue": float(df["revenue"].sum()),
        "revenue_by_product": df.groupby("product")["revenue"].sum().sort_values(ascending=False),
        "quantity_by_product": df.groupby("product")["quantity"].sum().sort_values(ascending=False),
        "low_stock": df[df["stock"] < LOW_STOCK_THRESHOLD][["product", "stock"]],
        "monthly_sales": df.groupby("month")["revenue"].sum()
    }