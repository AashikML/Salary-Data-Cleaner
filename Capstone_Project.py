import numpy as np
import pandas as pd


def clean_salary_data(df: pd.DataFrame) -> pd.DataFrame:
    print("=== Starting Advanced Data Cleaning ===")

    # 1. Remove duplicate records
    initial_rows = len(df)
    df = df.drop_duplicates()
    removed_duplicates = initial_rows - len(df)
    print(f"Removed {removed_duplicates} duplicate records.")

    # 2. Handle negative salaries if they exist
    if "Salary (INR)" in df.columns:
        negative_count = (df["Salary (INR)"] < 0).sum()
        if negative_count > 0:
            df["Salary (INR)"] = df["Salary (INR)"].abs()
            print(
                f"Corrected {negative_count} negative salary values by taking their absolute values."
            )
        else:
            print("No negative salary values detected.")

    # 3. Print summary statistics and data types
    print("\n=== Data Types ===")
    print(df.dtypes)

    print("\n=== Summary Statistics ===")
    print(df.describe().to_string())

    # 4. Remove salary outliers (too high or too low) using IQR method
    if "Salary (INR)" in df.columns:
        q1 = df["Salary (INR)"].quantile(0.25)
        q3 = df["Salary (INR)"].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        before_filter_count = len(df)
        df = df[
            (df["Salary (INR)"] >= lower_bound)
            & (df["Salary (INR)"] <= upper_bound)
        ].copy()
        removed_outliers = before_filter_count - len(df)

        print("\n=== Salary Outliers Handling ===")
        print(
            f"Salary bounds for outliers: Lower Bound = {lower_bound:.2f}, Upper Bound = {upper_bound:.2f}"
        )
        print(
            f"Removed {removed_outliers} rows with extreme (too high or too low) salaries."
        )

    print("\n=== Final Cleaned Dataset Preview ===")
    print(df.head().to_string())
    return df


if __name__ == "__main__":
    # Sample dataset for standalone execution; replace with pd.read_csv("your_file.csv")
    sample_data = pd.DataFrame(
        {
            "Employee": ["Aarav", "Diya", "Rohan", "Ananya", "Aarav", "Kabir"],
            "Salary (INR)": [45000, 52000, 48000, 350000, 45000, -12000],
        }
    )

    cleaned_df = clean_salary_data(sample_data)