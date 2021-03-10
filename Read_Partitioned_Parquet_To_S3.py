import os

import logging
import boto3
from botocore.exceptions import ClientError
print(os.listdir("Parquet Files/Invoices_100m_Initial"))
s3_client = boto3.client('s3')
bucket = "clumio-spark-bucket"
for part_name in os.listdir("Parquet Files/Invoices_100m_Initial"):
    #print("Dir Name", part_name)
    for file_name in os.listdir("Parquet Files/Invoices_100m_Initial"+"/"+part_name):
        print("Pq", file_name)
        try:
            file_name_f = "Parquet Files/Invoices_100m_Initial"+"/"+part_name+"/"+file_name
            response = s3_client.upload_file(file_name_f, bucket, "Backup_100m_Initial/Invoices/"+file_name)
        except ClientError as e:
            logging.error(e)
