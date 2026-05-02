from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("MD Conditions Sum").getOrCreate()

# Read parquet file into a DataFrame
df = spark.read.parquet("data/data.parquet")

# Show schema and first rows
df.printSchema()
df.show(5)

# Filter by degree == "MD" and sum n_conditions
md_conditions = df.filter(col("degree") == "MD").agg(spark_sum("n_conditions").alias("total_md_conditions"))
md_conditions.show()

spark.stop()