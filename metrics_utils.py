from pyspark.sql import functions as F
from config import MONITORING_TABLE

def log_pipeline_metric(spark, pipeline_name, df):
    metrics_df = spark.createDataFrame(
        [(pipeline_name, df.count())],
        ["pipeline", "row_count"]
    ).withColumn("processed_at", F.current_timestamp())

    metrics_df.write.mode("append").saveAsTable(MONITORING_TABLE)