from datetime import datetime
from pyspark.sql.functions import col, concat_ws, regexp_replace, udf
import unicodedata, re
from pyspark.sql.types import StringType


def normalize(text):
    if text is None:
        return None
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    return re.sub(r'[^a-zA-Z0-9]', '', text)

normalize_udf = udf(normalize, StringType())

def transform_save_parquet_silver(df, output):
    df = df.withColumn('state', normalize_udf(col('state'))) \
        .withColumn('country', normalize_udf(col('country'))) \
        .withColumn('Location', concat_ws('-', col('state'), col('country')))

    df.write.partitionBy("Location").mode("overwrite").format("parquet").save(output)

    return df
