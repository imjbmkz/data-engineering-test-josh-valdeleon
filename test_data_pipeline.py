from etl import (
    extract_excel, 
    load_to_database, 
    transform_rename_columns, 
    transform_ave_rating_by_neighborhood, 
    transform_ave_price_by_neighborhood
)

def test_extract_excel():
    df = extract_excel("airbnb.xlsx")
    assert df.shape==(30478, 13)

def test_transform_ave_rating_by_neighborhood():
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
    df_ave_rating_by_neighborhood = transform_ave_rating_by_neighborhood(df)

    expected = [
        {'neighbourhood': 'Brooklyn', 'avg_rating': 92.363497113232},
        {'neighbourhood': 'Manhattan', 'avg_rating': 91.80178495537612},
        {'neighbourhood': 'Bronx', 'avg_rating': 91.65437788018433},
        {'neighbourhood': 'Queens', 'avg_rating': 91.54905660377358},
        {'neighbourhood': 'Staten Island', 'avg_rating': 90.84375}
    ]

    assert df_ave_rating_by_neighborhood.to_dict(orient="records") == expected

def test_transform_ave_price_by_neighborhood():
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
    df_ave_rating_by_neighborhood = transform_ave_price_by_neighborhood(df)
    
    expected = [
        {'neighbourhood': 'Manhattan', 'avg_price': 198.4745836711782},
        {'neighbourhood': 'Staten Island', 'avg_price': 163.4625850340136},
        {'neighbourhood': 'Brooklyn', 'avg_price': 129.50047109207708},
        {'neighbourhood': 'Queens', 'avg_price': 103.22212467076383},
        {'neighbourhood': 'Bronx', 'avg_price': 94.6608695652174}
    ]

    assert df_ave_rating_by_neighborhood.to_dict(orient="records") == expected