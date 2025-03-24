import argparse
import yaml
import os
from modules.loader import load_all_csvs
from modules.cleaner import clean_data
from modules.transformer import transform_data
from modules.exporter import save_data


script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, "..", "config.yaml")

def main(config_path):
    # Load configuration
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Step 1: Load raw data
    raw_root = os.path.join(script_dir, "..", config["data"]["raw_root"])
    output_root = os.path.join(script_dir, "..", config["data"]["output_root"])

    for fname, raw_data in load_all_csvs(raw_root):
        cleaned = clean_data(raw_data, config["cleaning"])
        transformed = transform_data(cleaned, config["transformation"])

        output_path = os.path.join(output_root, fname)
        save_data(transformed, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Processing Pipeline")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    args = parser.parse_args()

    main(config_path)
