from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()
spark.sql("select 4").show()