# 📊 Sales & Inventory Analysis Pipeline

A production-style data pipeline for analyzing sales and inventory data, generating business insights, automated reports, and visualizations.

---

## 🚀 Overview

This project simulates a real-world business scenario where sales data is processed to extract insights that support decision-making.

It includes:

* Data ingestion and validation
* Data transformation and enrichment
* Business metrics calculation
* Automated reporting (CSV)
* Data visualization (charts)
* Logging and monitoring

---

## 🧠 Features

✅ Modular architecture (separation of concerns)
✅ CLI support (flexible execution)
✅ Structured logging (INFO, WARNING, ERROR)
✅ Business alerts (low stock detection)
✅ Automated report generation
✅ Visualization with charts
✅ Scalable and production-ready design

---

## 📂 Project Structure

```
sales-inventory-analysis/
│
├── data/
│   └── sales_data.csv
│
├── output/
│   ├── revenue_*.csv
│   ├── quantity_*.csv
│   ├── monthly_*.csv
│   ├── low_stock_*.csv
│   └── revenue_chart.png
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data_loader.py
│   ├── processor.py
│   ├── metrics.py
│   ├── report.py
│   ├── visualization.py
│   └── logger.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3.10+
* pandas
* matplotlib
* argparse
* logging

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/sales-inventory-analysis.git
cd sales-inventory-analysis
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the pipeline

```
python main.py --input data/sales_data.csv --output output/
```

---

## 📊 Output

The pipeline generates:

* 📁 Multiple CSV reports:

  * Revenue by product
  * Quantity sold
  * Monthly sales
  * Low stock alerts

* 📈 Visualization:

  * Revenue by product chart (`.png`)

---

## ⚠️ Logging Example

```
INFO | Starting pipeline...
INFO | Data loaded successfully
INFO | Data processed
INFO | Dataset size: 9 rows
INFO | Products analyzed: 4
WARNING | Low stock products detected: ['Notebook']
INFO | Reports exported to output
INFO | Chart saved at output/revenue_chart.png
INFO | Pipeline finished successfully
```

---

## 💡 Business Value

This project demonstrates how data can be used to:

* Monitor inventory levels
* Identify top-performing products
* Track revenue trends
* Support operational decision-making

---

## 🧩 Future Improvements

* Dashboard (Streamlit)
* API (FastAPI)
* Machine Learning (sales forecasting)
* Docker containerization
* Cloud deployment

---

## 👨‍💻 Author

**Matheus Mansano**

* Data Analyst / Backend Developer
* Python | Data Analysis | Automation

---

## ⭐ Final Notes

This project was designed to simulate a real production data pipeline, focusing on clean architecture, scalability, and business-driven insights.

---
