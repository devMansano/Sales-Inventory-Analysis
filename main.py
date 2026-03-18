import argparse
from pathlib import Path

from src.data_loader import load_data
from src.processor import process_data
from src.metrics import calculate_metrics
from src.report import export_report
from src.logger import setup_logger
from src.visualization import plot_revenue_by_product


def main() -> None:
    parser = argparse.ArgumentParser(description="Sales Analysis Pipeline")
    parser.add_argument("--input", default="data/sales_data.csv")
    parser.add_argument("--output", default="output/")

    args = parser.parse_args()

    logger = setup_logger()

    try:
        logger.info("Starting pipeline...")

        data_path = Path(args.input)
        output_path = Path(args.output)

        df = load_data(data_path)
        logger.info("Data loaded successfully")

        df = process_data(df)
        logger.info("Data processed")
        logger.info(f"Dataset size: {len(df)} rows")
        logger.info(f"Products analyzed: {df['product'].nunique()}")

        metrics = calculate_metrics(df)
        logger.info(f"Total revenue: {metrics['total_revenue']}")

        if not metrics["low_stock"].empty:
            logger.warning("Low stock products detected")

        export_report(metrics, output_path)
        logger.info(f"Reports exported to {output_path}")

        chart_path = plot_revenue_by_product(
            metrics["revenue_by_product"], 
            output_path
        )
        logger.info(f"Chart saved at {chart_path}")

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    main()