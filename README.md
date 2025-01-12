# Airbnb Data Pipeline Exercise 

## Introduction
This project is a simple ETL (Extract, Transform, Load) pipeline for analyzing Airbnb data. The pipeline processes an Excel dataset of Airbnb listings, cleans and transforms the data, computes aggregates, and stores the results in an SQLite database.

## Objective
The goal of this project is to:

1. Extract data from an Excel file (`airbnb.xlsx`).
2. Transform the dataset by renaming columns and calculating average review scores by neighborhood.
3. Load the processed data into an SQLite database (`airbnb.db`) for further analysis.
4. The SQLite database should consist of 3 tables.
   - `listings` shows all New York Airbnb listings based from the Excel file
   - `agg_ave_price_by_neighborhood`. Among the five neighborhoods in the dataset, which ones are the most expensive or cheapest? 
   - `agg_ave_rating_by_neighborhood`. Among the five neighborhoods in the dataset, which ones have the highest rated in Airbnb?

## Dataset
The datset contains 30,478 Airbnb listings in New York City. This was downloaded from [Tableau](https://public.tableau.com/app/learn/sample-data).

## Setup and execution
- Clone this repository
```
git clone git@github.com:imjbmkz/data-engineering-test-josh-valdeleon.git
```
- Create and activate virtual environment. 
```
python -m venv env 
.\env\Scripts\Activate.ps1
```
- Install the dependencies.
```
pip install -r requirements.txt
```
- Run the script.
```
python data_pipeline.py
```
- Run the pre-defined tests.
```
pytest -v
```