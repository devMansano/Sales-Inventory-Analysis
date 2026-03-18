from pathlib import Path
import pandas as pd

def export_report(metrics: dict, path: Path) -> None:
    report = metrics["revenue_by_product"].reset_index()
    report.columns = ["product", "total_revenue"]

    path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(path, index=False)