from pyspark.sql.functions import count

# Function to aggregate data and save data in parquet format
def count_save_gold(df, output):
    df_gold = df.groupBy("Location", "brewery_type").agg(count("*").alias("brewery_count"))

    df_gold.write.mode("overwrite").format("parquet").save(output)
    
    return df_gold
