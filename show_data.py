from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadParquetDemo").getOrCreate()

# Read parquet file into a DataFrame
df = spark.read.parquet("data/data.parquet")

# Show schema and first rows
df.printSchema()
df.show()

spark.stop()