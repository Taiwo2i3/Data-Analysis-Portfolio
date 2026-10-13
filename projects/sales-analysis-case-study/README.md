# Monthly Sales Performance Analysis

## Business question

Which product and month generated the most revenue in a small illustrative sales dataset?

## Data

The file `data/sample_monthly_sales.csv` is synthetic and was created for demonstration. It is not real company performance data. The values use illustrative NGN unit prices.

## Method

1. Validate required columns and check missing or negative values.
2. Calculate revenue as units sold multiplied by unit price.
3. Aggregate revenue by product and month.
4. Visualize the monthly revenue trend and export a product summary.

## Run

From the repository root:

```bash
pip install -r requirements.txt
python python/sales_analysis.py
```

Outputs are written to `outputs/`, which is ignored by Git.

## Interpretation checklist

When replacing the synthetic data with approved real data, check seasonality, price changes, stock availability, marketing campaigns, and whether the same period is being compared. Revenue alone is not profit; cost and margin data would be needed before making profitability claims.

## Limitations

This starter example is descriptive, not causal. Do not interpret a trend in this small synthetic dataset as a forecast or as actual business performance.
