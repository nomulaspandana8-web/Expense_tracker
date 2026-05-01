import pandas as pd

def convert_to_dataframe(data):
    df = pd.DataFrame(data, columns=["ID", "Title", "Amount", "Category"])
    return df

def calculate_total(df):
    return df["Amount"].sum() if not df.empty else 0