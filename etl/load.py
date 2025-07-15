from pyspark.sql.functions import count

def count_save_gold(df, output):
    """Cria agregação por tipo e localização e salva em Parquet na camada Gold"""
    df_gold = df.groupBy("Location", "brewery_type").agg(count("*").alias("brewery_count"))

    df_gold.write.mode("overwrite").format("parquet").save(output)
    
    return df_gold
