"""Functions for loading the project datasets."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_retail_data(
    filename: str = "sample_retail_pricing.csv",
) -> pd.DataFrame:
    """Load the retail pricing dataset from the raw data folder."""

    file_path = RAW_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Retail dataset was not found: {file_path}"
        )

    return pd.read_csv(file_path, parse_dates=["date"])