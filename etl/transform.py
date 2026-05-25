import pandas as pd

def build_model(sales: pd.DataFrame,
                reseller: pd.DataFrame,
                region: pd.DataFrame,
                products: pd.DataFrame
                ) -> pd.DataFrame:
    df = sales.merge(reseller, on = 'ResellerKey', how = 'left')
    df = df.merge(products, on = 'ProductKey', how = 'left')
    df = df.merge(region, on = 'SalesTerritoryKey', how = 'left')

    df['Income'] = df['Sales'] - df['Cost']

    return df
