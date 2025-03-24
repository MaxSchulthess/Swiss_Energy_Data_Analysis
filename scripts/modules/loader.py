import os
import pandas as pd

def load_all_csvs(raw_root):
    all_dfs = []

    for dirpath, _, filenames in os.walk(raw_root):
        for fname in filenames:
            if fname.endswith(".csv"):
                full_path = os.path.join(dirpath, fname)
                df = pd.read_csv(full_path)
                all_dfs.append((fname, df))  # Keep filename if needed

    return all_dfs  # List of (filename, DataFrame) tuples
