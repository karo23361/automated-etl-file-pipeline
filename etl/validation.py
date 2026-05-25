
from great_expectations.dataset import PandasDataset

def validate_model(df):
    ds = PandasDataset(df)
    
    ds.expect_column_values_to_not_be_null("ResellerKey")
    ds.expect_column_values_to_not_be_null("ProductKey")
    ds.expect_column_values_to_not_be_null("SalesTerritoryKey")
    ds.expect_column_values_to_be_between("Quantity", min_value=1)
    ds.expect_column_values_to_be_between("Unit Price", min_value=0)

    result = ds.validate()
    if not result["success"]:
        raise ValueError(f"Data validation failed: {result}")
