import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from pyspark.sql import SparkSession

sys.path.append('/opt/airflow')

from etl.extract import save_extract_files_bronze
from etl.transform import transform_save_parquet_silver
from etl.load import count_save_gold


# Create spark session
def create_spark_session():
    return SparkSession.builder \
        .appName('ETL-Case-AbInbev-IgorFerreiraFranca') \
        .getOrCreate()

# Extract data and save data on json format
def run_extract():
    spark = create_spark_session()
    date_today = str(datetime.now().date())
    bronze_path = f'/opt/airflow/datalake/bronze/breweries_{date_today}'
    save_extract_files_bronze(spark, bronze_path)
    spark.stop()

# Apply some transformations and save data on parquet format
def run_transform():
    spark = create_spark_session()
    date_today = str(datetime.now().date())
    bronze_path = f'/opt/airflow/datalake/bronze/breweries_{date_today}'
    silver_path = f'/opt/airflow/datalake/silver/breweries_{date_today}'
    df_bronze = spark.read.json(bronze_path)
    transform_save_parquet_silver(df_bronze, silver_path)
    spark.stop()

# Aggregate data and save on parquet format
def run_load():
    spark = create_spark_session()
    date_today = str(datetime.now().date())
    silver_path = f'/opt/airflow/datalake/silver/breweries_{date_today}'
    gold_path = f'/opt/airflow/datalake/gold/breweries_{date_today}'
    df_silver = spark.read.parquet(silver_path)
    df_gold = count_save_gold(df_silver, gold_path)

    df_gold.createOrReplaceTempView('gold')
    spark.sql('''
        SELECT
            *
        FROM gold
        ORDER BY brewery_count DESC
    ''').show(50, truncate=False)
    spark.stop()

# Set arguments
default_args = {
    'owner': 'igorferreirafranca',
    'start_date': datetime(2025, 7, 15, 9, 0),
    'retries': 3,
    'email_on_failure': True,
    'email': ['igorffrancaa@gmail.com']
}

# Pipeline is set to run every day at 09am
with DAG(
    dag_id='case_abinbev',
    default_args=default_args,
    schedule_interval='0 9 * * *',
    catchup=False,
    max_active_runs=1
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id='load_and_aggregate',
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task
