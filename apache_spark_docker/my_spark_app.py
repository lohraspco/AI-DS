from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
import os
import sys

print(sys.version)
conf = SparkConf()
app_name = "shiri"
print(os.environ.get("SPARK_MASTER_URL"))
conf.setAll(
    [
        # (
        #     "spark.master",
        #     os.environ.get("SPARK_MASTER_URL", "spark://localhost:7067"),
        # ),
        (
            "spark.driver.host",
            os.environ.get("SPARK_DRIVER_HOST", "host.docker.internal"),
        ),
        ("spark.submit.deployMode", "client"),
        # ("spark.driver.bindAddress", "0.0.0.0"),
        ("spark.app.name", app_name),
    ]
)

print(conf)
spark = (
    SparkSession.builder.appName("MySparkApp22")
    .master("spark://localhost:7067")
    .config("spark.driver.host","10.0.0.183")
    .config("spark.executor.heartbeatInterval", "30s")
    .config("spark.network.timeout", "300s")
    # .config(conf=conf) 
    .getOrCreate()
)

data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)
result = rdd.sum()
def print_red(text):
    red_color_code = "\033[91m"  # Bright Red
    reset_color_code = "\033[0m"  # Reset to default color
    print(f"{red_color_code}{text}{reset_color_code}")
print_red(f"Sum:{result}")

spark.stop()
