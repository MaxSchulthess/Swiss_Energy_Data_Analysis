def clean_data(df, cleaning_config):
    if cleaning_config["drop_duplicates"]:
        df = df.drop_duplicates()
    if cleaning_config["fill_missing"]:
        df = df.fillna(cleaning_config["fill_value"])
    return df
