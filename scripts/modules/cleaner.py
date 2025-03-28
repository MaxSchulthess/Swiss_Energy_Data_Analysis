import pandas as pd

def parse_datetime_columns(df):
    for col in df.columns:
        if df[col].dtype == object:
            sample = df[col].dropna().astype(str).head(5)
            if sample.apply(lambda x: any(c in x for c in ["/", "-", ".", " "])).all():
                try:
                    df[col] = pd.to_datetime(df[col], errors="coerce")
                except Exception:
                    continue
    return df

def clean_data(df, cleaning_config):
    df = df.dropna(how="all")
    if cleaning_config["drop_duplicates"]:
        df = df.drop_duplicates()
    if cleaning_config["fill_missing"]:
        df = df.fillna(cleaning_config["fill_value"])
    return df
