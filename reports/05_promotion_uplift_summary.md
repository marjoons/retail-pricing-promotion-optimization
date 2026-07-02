# Promotion Uplift Modeling Summary

## Dataset

- Source: `data\raw\synthetic\sample_retail_pricing.csv`
- Modeling observations: 18,300
- Training observations: 14,600
- Test observations: 3,700
- Promotion rate: 16.01%
- Split method: chronological

## Model Performance

- RMSE: 9.5699
- MAE: 6.6666
- R-squared: 0.7751
- Propensity overlap share: 94.41%

## Promotion Effect

- Raw difference: 26.3597 units
- T-learner average uplift: 25.3442 units
- Doubly robust average uplift: 27.5700 units
- Approximate 95% confidence interval: [26.1067, 29.0332]

## Interpretation

The doubly robust estimate combines an outcome model with a promotion-assignment model. This reduces reliance on either model being perfectly specified.

The individual uplift estimates can support targeted promotion decisions by identifying products, stores, and time periods where promotions are expected to generate positive incremental demand.

Revenue and margin estimates are scenario-based calculations and should be reviewed together with promotion cost, discount funding, inventory capacity, and operational constraints.
