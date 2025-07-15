from etl.extract import save_extract_files_bronze
from etl.transform import transform_save_parquet_silver
from etl.load import count_save_gold
from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder \
        .appName('ETL-Case-AbInbev-IgorFerreiraFranca') \
        .getOrCreate()

date_today = str(datetime.now().date())
bronze_path = f'datalake/bronze/breweries_{date_today}'
silver_path = f'datalake/silver/breweries_{date_today}'
gold_path = f'datalake/gold/breweries_{date_today}'

save_extract_files_bronze(spark, bronze_path)

df_bronze = spark.read.json(bronze_path)
df_silver = transform_save_parquet_silver(df_bronze, silver_path)

df_gold = count_save_gold(df_silver, gold_path)
df_gold.createOrReplaceTempView('gold')

spark.sql('''
    SELECT
        *
    FROM gold
    ORDER BY brewery_count DESC
''').show(100, truncate=False)

spark.stop()