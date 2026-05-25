import pandas as pd
import logging

logger = logging.getLogger(__name__)
def validate_model(df):
    logger.info("Validating model...")

    if df["ResellerKey"].isnull().any():
        raise ValueError("ResellerKey contains null values")
    if df["ProductKey"].isnull().any():
        raise ValueError("ProductKey contains null values")
    if df["SalesTerritoryKey"].isnull().any():
        raise ValueError("SalesTerritoryKey contains null values")
    if (df["Quantity"] < 1).any():
        raise ValueError("Quantity contains values less than 1")
    if (df["Unit Price"] < 0).any():
        raise ValueError("Unit Price contains values less than 0")

    logger.info("Validation passed successfully")

