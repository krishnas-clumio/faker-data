import pyarrow
import pandas as pd
try:
    df = pd.read_csv('CSV Files/invoices_100m_final.csv')
    df.to_parquet('Parquet Files/Invoices_100m_Initial', partition_cols="product_id")
except Exception as e:
    print("Error", e)

