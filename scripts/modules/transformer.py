from sklearn.preprocessing import StandardScaler

def transform_data(df, transform_config):
    if transform_config["normalize"]:
        scaler = StandardScaler()
        df[df.columns] = scaler.fit_transform(df)
    return df
