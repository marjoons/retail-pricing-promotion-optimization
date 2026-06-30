"""Functions for loading the project datasets."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
M5_DATA_DIR = RAW_DATA_DIR / "m5"
SYNTHETIC_DATA_DIR = RAW_DATA_DIR / "synthetic"


def load_csv(
    file_path: Path,
    nrows: int | None = None,
    parse_dates: list[str] | None = None,
) -> pd.DataFrame:
    """Load a CSV file after confirming that it exists."""

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(
        file_path,
        nrows=nrows,
        parse_dates=parse_dates,
    )


def load_m5_calendar(
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load the M5 calendar dataset."""

    return load_csv(
        M5_DATA_DIR / "calendar.csv",
        nrows=nrows,
        parse_dates=["date"],
    )


def load_m5_prices(
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load the M5 weekly selling-price dataset."""

    return load_csv(
        M5_DATA_DIR / "sell_prices.csv",
        nrows=nrows,
    )


def load_m5_sales(
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load the M5 historical sales dataset."""

    return load_csv(
        M5_DATA_DIR / "sales_train_validation.csv",
        nrows=nrows,
    )


def load_synthetic_retail_data(
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load the synthetic retail pricing dataset."""

    return load_csv(
        SYNTHETIC_DATA_DIR / "sample_retail_pricing.csv",
        nrows=nrows,
        parse_dates=["date"],
    )


def load_market_notes(
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load the synthetic market-notes dataset."""

    return load_csv(
        SYNTHETIC_DATA_DIR / "market_notes.csv",
        nrows=nrows,
        parse_dates=["date"],
    )