from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg as spark_avg

spark = SparkSession.builder.appName("Degree Avg Treatments").getOrCreate()

# Read parquet file into a DataFrame
df = spark.read.parquet("data/data.parquet")

# Show schema and first rows
df.printSchema()
df.show(5)

# Group by degree and calculate average n_treatments
degree_avg_treat = df.groupBy("degree").agg(spark_avg("n_treatments").alias("avg_n_treatments"))
degree_avg_treat.show()

spark.stop()