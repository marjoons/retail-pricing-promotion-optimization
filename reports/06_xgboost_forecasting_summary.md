# XGBoost Demand-Forecasting Summary

## Dataset

- Source: `data\raw\synthetic\sample_retail_pricing.csv`
- Historical observations: 18,300
- Stores: 5
- Products: 10
- Date range: 2024-01-01 to 2024-12-31
- Training observations: 12,800
- Validation observations: 2,750
- Test observations: 2,750

## XGBoost Test Performance

- MAE: 4.7458
- RMSE: 6.3440
- R-squared: 0.9052
- WAPE: 13.31%
- MAPE: 15.42%
- Forecast accuracy: 86.69%
- Forecast bias: -0.43%

## Baseline Comparison

- Best baseline: Seasonal lag-7 baseline
- Best baseline RMSE: 20.6523
- XGBoost RMSE improvement: 69.28%

## Production Forecast

- Forecast interval: 1 day(s)
- Store-product forecasts created: 50
- Total next-period forecast demand: 1,545.30 units
- Production boosting rounds: 375

## Interpretation

The forecasting model combines calendar variables, product and store information, planned commercial variables, and leakage-safe historical-demand features.

The chronological test period contains observations occurring after the training and validation periods. This provides a realistic assessment of future forecast performance.

The next-period forecast assumes the latest promotion, price, inventory and external conditions continue into the forecast period. These assumptions should be replaced with approved commercial plans when available.

Forecast results should be reviewed alongside inventory availability, promotion capacity, service-level requirements and pricing constraints before operational use.
