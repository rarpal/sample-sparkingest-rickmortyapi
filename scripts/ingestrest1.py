#%%
import pyspark
import requests
from pyspark.sql.functions import udf, col, explode
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql import Row
spark = pyspark.sql.SparkSession.builder.getOrCreate()
#%%
# schema = StructType([
#     StructField("id", IntegerType(), True),
#     StructField("name", StringType(), True),
#     StructField("status", StringType(), True),
#     StructField("species", StringType(), True),
#     StructField("type", StringType(), True),
#     StructField("gender", StringType(), True),
#     StructField("origin", StructType([
#         StructField("name", StringType(), True),
#         StructField("url", StringType(), True)     
#         ])),
#     StructField("location", StructType([
#         StructField("name", StringType(), True),
#         StructField("url", StringType(), True)     
#         ])),
#     StructField("image", StringType(), True),
#     StructField("episode", ArrayType(StringType())),
#     StructField("url", StringType(), True),
#     StructField("created", StringType(), True)
#   ])

schema = ArrayType(StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("status", StringType(), True),
    StructField("species", StringType(), True),
    StructField("type", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("created", StringType(), True)
  ]))
#%%
def executeRestApi(url):
  res = None
  # Make API request, get response object back, create dataframe from above schema.
  try:
    res = requests.get(url)
  except Exception as e:
    return e

  if res != None and res.status_code == 200:
    #return json.loads(res.text)
    return res.json()

  return None
#%%
udf_executeRestApi = udf(executeRestApi, schema)

def getNewRow(url):
    r = Row("url")
    df = spark.createDataFrame(
        [r(url)]
        ).withColumn("execute", udf_executeRestApi(url))
    return df

def createDFRestApi(url):
    df = getNewRow(url)
    resp = None
    nexturl = url
    restlist = []

    while nexturl:
        resp = requests.get(nexturl)
        rest = resp.json()
        nexturl = rest['info']['next']
        df.union(getNewRow(nexturl))

    return df
#%%
request_df = createDFRestApi("https://rickandmortyapi.com/api/character")
#%%
results_df = request_df.select(explode(col("execute")).alias("results")).select(
                  col("results.id").alias("id"),
                  col("results.name").alias("name"),
                  col("results.status").alias("status"),
                  col("results.species").alias("species"),
                  col("results.type").alias("type"),
                  col("results.gender").alias("gender"),
                  col("results.created").alias("created")
                  )
# %%
results_df.count()
# %%
