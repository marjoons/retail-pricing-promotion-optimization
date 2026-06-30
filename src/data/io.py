"""Utilities for loading, validating, and saving project datasets."""

from pathlib import Path
from typing import Final

import pandas as pd


# ---------------------------------------------------------------------------
# Project directories
# ---------------------------------------------------------------------------

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]

RAW_DATA_DIR: Final[Path] = PROJECT_ROOT / "data" / "raw"
INTERIM_DATA_DIR: Final[Path] = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA_DIR: Final[Path] = PROJECT_ROOT / "data" / "processed"


# ---------------------------------------------------------------------------
# Generic input/output functions
# ---------------------------------------------------------------------------

def load_csv(
    file_path: str | Path,
    *,
    parse_dates: list[str] | None = None,
) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Relative paths are interpreted from the project root.

    Parameters
    ----------
    file_path:
        Absolute path or path relative to the project root.
    parse_dates:
        Optional list of columns that should be converted to datetime.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the requested file does not exist.
    """
    path = Path(file_path)

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path, parse_dates=parse_dates)


def save_csv(
    dataframe: pd.DataFrame,
    file_path: str | Path,
    *,
    index: bool = False,
) -> Path:
    """
    Save a pandas DataFrame as a CSV file.

    The destination directory is created automatically when necessary.

    Parameters
    ----------
    dataframe:
        DataFrame to save.
    file_path:
        Absolute path or path relative to the project root.
    index:
        Whether to include the DataFrame index.

    Returns
    -------
    pathlib.Path
        Final location of the saved file.
    """
    path = Path(file_path)

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(path, index=index)

    return path


# ---------------------------------------------------------------------------
# Dataset-specific functions
# ---------------------------------------------------------------------------

def load_retail_data(
    filename: str = "sample_retail_pricing.csv",
) -> pd.DataFrame:
    """
    Load the main retail pricing dataset from data/raw.
    """
    return load_csv(
        RAW_DATA_DIR / filename,
        parse_dates=["date"],
    )


def load_market_notes(
    filename: str = "market_notes.csv",
) -> pd.DataFrame:
    """
    Load market notes used for the future LLM-RAG component.
    """
    return load_csv(RAW_DATA_DIR / filename)


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: list[str],
) -> None:
    """
    Verify that a DataFrame contains all required columns.

    Raises
    ------
    ValueError
        If one or more required columns are missing.
    """
    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )