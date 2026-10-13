"""Analyze the synthetic monthly sales dataset and save a chart.

Run from the repository root:
    python python/sales_analysis.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_monthly_sales.csv"
OUTPUT_DIR = ROOT / "outputs"


def main() -> None:
    df = pd.read_csv(DATA_PATH, parse_dates=["month"])
    required = {"month", "region", "product", "units_sold", "unit_price"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    if df[list(required)].isnull().any().any():
        raise ValueError("Dataset contains missing values in required columns.")
    if (df["units_sold"] < 0).any() or (df["unit_price"] < 0).any():
        raise ValueError("Units and unit prices must not be negative.")

    df["revenue"] = df["units_sold"] * df["unit_price"]
    monthly = df.groupby(df["month"].dt.to_period("M"))["revenue"].sum()
    product_summary = (
        df.groupby("product", as_index=False)
        .agg(units_sold=("units_sold", "sum"), revenue=("revenue", "sum"))
        .sort_values("revenue", ascending=False)
    )

    print("\nRevenue by product (synthetic data):")
    print(product_summary.to_string(index=False, formatters={"revenue": "{:,.0f}".format}))
    print("\nMonthly revenue:")
    print(monthly.to_string())

    OUTPUT_DIR.mkdir(exist_ok=True)
    ax = monthly.plot(kind="line", marker="o", title="Monthly Revenue (Synthetic Sample)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (NGN, illustrative)")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    chart_path = OUTPUT_DIR / "monthly_revenue.png"
    plt.savefig(chart_path, dpi=160)
    plt.close()
    product_summary.to_csv(OUTPUT_DIR / "product_summary.csv", index=False)
    print(f"\nSaved chart: {chart_path}")
    print(f"Saved summary: {OUTPUT_DIR / 'product_summary.csv'}")


if __name__ == "__main__":
    main()
