import sqlite3
from etl import (
    extract_excel, 
    load_to_database, 
    transform_rename_columns, 
    transform_ave_rating_by_neighborhood, 
    transform_ave_price_by_neighborhood
)

if __name__=="__main__":
    # Load the data from Excel, then standardize the columns
    df = extract_excel("airbnb.xlsx")
    new_columns = [
        "host_id",
        "host_since",
        "name",
        "neighbourhood",
        "property_type",
        "review_scores_rating__bin",
        "room_type",
        "zipcode",
        "beds",
        "number_of_records",
        "number_of_reviews",
        "price",
        "review_scores_rating",
    ]
    df = transform_rename_columns(df, new_columns)
    
    # Create aggregates of the data
    df_ave_rating_by_neighborhood = transform_ave_rating_by_neighborhood(df)
    df_ave_price_by_neighborhood = transform_ave_price_by_neighborhood(df)

    con = sqlite3.connect("airbnb.db")
    load_to_database(df, con, "listings")
    load_to_database(df_ave_rating_by_neighborhood, con, "agg_ave_rating_by_neighborhood")
    load_to_database(df_ave_price_by_neighborhood, con, "agg_ave_price_by_neighborhood")
    con.close()