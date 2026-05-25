import pandas as pd

def clean_currency(series):
    return (
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .pipe(pd.to_numeric, errors="coerce")
    )


def build_model(sales,
                reseller,
                region,
                products
                ):
    df = sales.merge(reseller, on = 'ResellerKey', how = 'left')
    df = df.merge(products, on = 'ProductKey', how = 'left')
    df = df.merge(region, on = 'SalesTerritoryKey', how = 'left')

    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Sales"] = clean_currency(df["Sales"])
    df["Cost"] = clean_currency(df["Cost"])
    df["Unit Price"] = clean_currency(df["Unit Price"])

    df['Income'] = df['Sales'] - df['Cost']

    return df
