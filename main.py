import argparse
from pathlib import Path

from src.data_loader import load_data
from src.processor import process_data
from src.metrics import calculate_metrics
from src.report import export_report
from src.logger import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Sales Analysis Pipeline")
    parser.add_argument("--input", default="data/sales_data.csv")
    parser.add_argument("--output", default="output/report.csv")

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

        metrics = calculate_metrics(df)
        logger.info(f"Total revenue: {metrics['total_revenue']}")

        export_report(metrics, output_path)
        logger.info(f"Report exported to {output_path}")

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()