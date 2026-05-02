from pyspark.sql import SparkSession


# Initialize Spark Session (local mode)
spark = SparkSession.builder \
    .appName("HelloWorld") \
    .master("local[*]") \
    .getOrCreate()


# Create data
data = [("Hello",), ("World",), ("from",), ("PySpark",)]
df = spark.createDataFrame(data, ["Word"])


# Show results
df.show()


# Print a count to confirm it worked
print(f"Total Rows: {df.count()}")


# Convert DataFrame to RDD and save as text file
# This writes one or more part files to the directory "output/hello_text"
df.rdd.saveAsTextFile("output/hello_text")


# Stop the session
spark.stop()
