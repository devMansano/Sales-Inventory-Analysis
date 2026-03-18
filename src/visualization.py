from pathlib import Path
import matplotlib.pyplot as plt

def plot_revenue_by_product(series, output_path: Path):
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / "revenue_chart.png"

    series.plot(kind="bar")
    plt.title("Revenue by Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()

    return file_path