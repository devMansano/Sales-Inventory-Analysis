import pandas as pd
from pathlib import Path
from datetime import datetime

def export_report(metrics: dict, path):
    path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    metrics["revenue_by_product"].to_csv(path / f"revenue_{timestamp}.csv")
    metrics["quantity_by_product"].to_csv(path / f"quantity_{timestamp}.csv")
    metrics["monthly_sales"].to_csv(path / f"monthly_{timestamp}.csv")
    metrics["low_stock"].to_csv(path / f"low_stock_{timestamp}.csv", index=False)