import pandas as pd

def transform_rename_columns(df: pd.DataFrame, new_columns: list) -> pd.DataFrame:
    df_new = df.copy()
    df_new.columns = new_columns
    return df_new

def transform_ave_rating_by_neighborhood(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('neighbourhood')['review_scores_rating'].mean().reset_index(name='avg_rating').sort_values(by='avg_rating', ascending=False)

def transform_ave_price_by_neighborhood(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('neighbourhood')['price'].mean().reset_index(name='avg_price').sort_values(by='avg_price', ascending=False)