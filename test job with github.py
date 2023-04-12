import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1681312859734 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": [
            "s3://contentful-ui-extensions.dacsoftware.tech/tinymce-legacy/extension.json"
        ]
    },
    transformation_ctx="AmazonS3_node1681312859734",
)

# Script generated for node Filter
Filter_node1681313242776 = Filter.apply(
    frame=AmazonS3_node1681312859734,
    f=lambda row: (),
    transformation_ctx="Filter_node1681313242776",
)

job.commit()
