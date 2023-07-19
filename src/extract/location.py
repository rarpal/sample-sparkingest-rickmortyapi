from pyspark.sql.functions import udf, col, explode
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql import Row
from common.client import get_rest_api

def extract_data(spark):

    schema = ArrayType(StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("type", StringType(), True),
        StructField("dimension", StringType(), True),
        StructField("url", StringType(), True),
        StructField("created", StringType(), True)
    ]))

    udf_executeRestApi = udf(get_rest_api, schema)

    RestApiRequest = Row("url")
    request_df = spark.createDataFrame([
                RestApiRequest("https://rickandmortyapi.com/api/location")
            ])\
            .withColumn("execute", udf_executeRestApi(col("url")))

    results_df = request_df.select(explode(col("execute")).alias("results")).select(
                    col("results.id").alias("id"),
                    col("results.name").alias("name"),
                    col("results.type").alias("type"),
                    col("results.dimension").alias("dimension"),
                    col("results.url").alias("url"),
                    col("results.created").alias("created")
                    )
    
    # write to data lake
