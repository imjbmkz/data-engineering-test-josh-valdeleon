import pandas as pd

def extract_excel(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)