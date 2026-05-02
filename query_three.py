from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg as spark_avg

spark = SparkSession.builder.appName("Geo Averages").getOrCreate()

# Read parquet file into a DataFrame
df = spark.read.parquet("data/data.parquet")

# Show schema and first rows
df.printSchema()
df.show(5)

# Calculate average longitude and latitude
geo_avgs = df.agg(
    spark_avg("longitude").alias("avg_longitude"),
    spark_avg("latitude").alias("avg_latitude")
)
geo_avgs.show()

spark.stop()