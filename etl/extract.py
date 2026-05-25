import pandas as pd
from .utils import find_latest_file


def extract_sources(input_dir):
    sources = {}

    for prefix in ["products", "sales", "region", "reseller"]:
        path = find_latest_file(input_dir, prefix)
        if path is None:
            raise FileNotFoundError(f"No file found for prefix {prefix}")
        df = pd.read_csv(path, sep="\t")
        sources[prefix] = df
    return sources