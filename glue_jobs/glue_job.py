import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="customer_target",
    table_name="postgredb_demo_public_customers"
)

df = dynamic_frame.toDF()
df.show()

job.commit()
