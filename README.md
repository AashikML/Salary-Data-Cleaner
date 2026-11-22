<div align="center">

# 🧹 Salary Data Cleaner

**A modular, terminal-ready data preprocessing pipeline built with Python, Pandas, and NumPy.**

![Python](https://img.shields.io/badge/Python-3.8%2B-0F172A?style=for-the-badge&logo=python&logoColor=38BDF8)
![Pandas](https://img.shields.io/badge/Pandas-Data_Pipeline-0F172A?style=for-the-badge&logo=pandas&logoColor=38BDF8)
![NumPy](https://img.shields.io/badge/NumPy-Analytics-0F172A?style=for-the-badge&logo=numpy&logoColor=38BDF8)
![Status](https://img.shields.io/badge/Status-Production_Ready-0F172A?style=for-the-badge&logo=github&logoColor=22C55E)

*Automates duplicate removal, negative-value correction, schema/statistical inspection, and IQR-based outlier filtering for ML-ready tabular data.*

</div>

---

## ⚡ Features & Pipeline Workflow

1. **Duplicate Record Removal**
   - Tracks initial dataset row count (`len(df)`).
   - Drops exact duplicate rows via `df.drop_duplicates()` and logs the exact count of removed records.

2. **Negative Salary Sanitization**
   - Validates the presence of the `Salary (INR)` column.
   - Detects negative entries (`< 0`) and normalizes them via `.abs()`, reporting all corrected values.

3. **Schema & Summary Statistics Inspection**
   - Prints column data types (`df.dtypes`) to verify schema integrity.
   - Outputs full descriptive statistics (`mean`, `std`, `min`, quartiles, `max`) via `df.describe().to_string()` for crisp CLI readability.

4. **IQR-Based Outlier Filtering**
   - Computes the 25th percentile ($Q_1$), 75th percentile ($Q_3$), and Interquartile Range ($\text{IQR} = Q_3 - Q_1$).
   - Establishes statistical thresholds:
     $$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$$
     $$\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$
   - Filters extreme salary anomalies and logs exact boundary limits alongside dropped row counts.

5. **Standalone & Modular Architecture**
   - Encapsulated inside `clean_salary_data(df: pd.DataFrame) -> pd.DataFrame` with type hints for seamless integration into larger ETL or ML pipelines.
   - Includes a ready-to-use CSV dataset right inside the repository for instant testing.

---

## 📁 Project Structure

```text
Salary-Data-Cleaner/
├── cCapstone_Project.py   # Main data-cleaning module and CLI runner
├── indian_employee_data.csv       # Sample raw salary dataset provided for testing
└── README.md              # Project documentation

Note: A ready-to-run sample CSV file (indian_employee_data.csv) is included directly in this repository so you can test the pipeline out of the box.

👨‍💻 About the Author
Name: Aashik Pandit

Age: 15

Country: Nepal

Mission & Aspirations: Aspiring Machine Learning & AI Engineer, focused on building scalable AI systems, end-to-end data pipelines, and clean production-ready code, with a long-term goal of working at top tech companies like Google or Microsoft.

GitHub: https://github.com/AashikML

LinkedIn: https://www.linkedin.com/in/aashikml

X: https://x.com/TheAashikML
