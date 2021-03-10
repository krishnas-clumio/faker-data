from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
import gresearch.spark.diff

sc = SparkContext()
print("******TESTING******")
conf = SparkConf().setAppName('integration test').setMaster('local[2]')
conf = conf.setAll([
    ('spark.ui.showConsoleProgress', 'false'),
    ('spark.locality.wait', '0'),
])
spark = SparkSession.builder.config(conf=conf).getOrCreate()
left = spark.createDataFrame([(1, "one"), (2, "two"), (3, "three")], ["id", "value"])
right = spark.createDataFrame([(1, "one"), (2, "Two"), (4, "four")], ["id", "value"])

left.diff(right).show()
sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', 's3-us-west-2.amazonaws.com')
sqlContext = SQLContext(sc)
df_initial = sqlContext.read.parquet('s3a://clumio-spark-bucket/Backup-Initial/TestTable')
print("TYPE******", type(df_initial))
df_incremental = sqlContext.read.parquet('s3a://clumio-spark-bucket/Backup-Incremental-1/TestTable')
print("#########*********COUNT********#######", df_incremental.count())
#df_incremental.diff(df_initial).write.parquet("s3a://clumio-spark-bucket/Output/TestTable")
df_output = df_initial.diff(df_incremental)
df_output.show()
#df_output.filter("diff == 'I'").write.parquet("s3a://clumio-spark-bucket/Output/TestTable")
df_output.filter("diff == 'I' or diff == 'C'").write.parquet("s3a://clumio-spark-bucket/Output/TestTable")
~                                                                                                           