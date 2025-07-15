import requests
from datetime import datetime
from pyspark.sql.types import StructField, StructType, StringType, DoubleType
import json


def extract_data():
    page = 1
    data_list = []
    while page < 101:
        url = f'https://api.openbrewerydb.org/v1/breweries?per_page=50&page={page}'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error when retrieved data from API. Status code: {response.status_code}")
        data = response.json()
        data_list.extend(data)
        print(f'Page: {page} extracted')
        page += 1
    return data_list

def clean_data(data):
    cleaned_data = []
    for item in data:
        cleaned_item = {
            "id": item.get("id", None),
            "name": item.get("name", None),
            "brewery_type": item.get("brewery_type", None),
            "address_1": item.get("address_1", None),
            "address_2": item.get("address_2", None),
            "address_3": item.get("address_3", None),
            "state_province": item.get("state_province", None),
            "city": item.get("city", None),
            "postal_code": item.get("postal_code", None),
            "country": item.get("country", None),
            "longitude": float(item.get("longitude", None)) if item.get("longitude") else None,
            "latitude": float(item.get("latitude", None)) if item.get("latitude") else None,
            "phone": item.get("phone", None),
            "website_url": item.get("website_url", None),
            "state": item.get("state", None),
            "street": item.get("street", None)
        }
        cleaned_data.append(cleaned_item)
    return cleaned_data


schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("brewery_type", StringType(), True),
    StructField("address_1", StringType(), True),
    StructField("address_2", StringType(), True),
    StructField("address_3", StringType(), True),
    StructField("state_province", StringType(), True),
    StructField("city", StringType(), True),
    StructField("postal_code", StringType(), True),
    StructField("country", StringType(), True),
    StructField("longitude", DoubleType(), True),
    StructField("latitude", DoubleType(), True),
    StructField("phone", StringType(), True),
    StructField("website_url", StringType(), True),
    StructField("state", StringType(), True),
    StructField("street", StringType(), True)
])

def save_extract_files_bronze(spark, output):
    data = extract_data()
    cleaned_data = clean_data(data)
    df_data_pyspark = spark.createDataFrame(cleaned_data, schema)
    df_data_pyspark.write.mode("overwrite").json(output)