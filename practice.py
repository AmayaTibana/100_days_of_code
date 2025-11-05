import boto3
import psycopg2

# AWS S3 setup
s3 = boto3.client('s3')
bucket_name = 'my-data-bucket'
file_key = 'data/sample.csv'

# Download file from S3
s3.download_file(bucket_name, file_key, '/tmp/sample.csv')

# Connect to Redshift
conn = psycopg2.connect(
    dbname='mydb',
    user='myuser',
    password='mypassword',
    host='redshift-cluster.endpoint.aws.com',
    port='5439'
)
cur = conn.cursor()

# Load data into Redshift
with open('/tmp/sample.csv', 'r') as f:
    cur.copy_expert("COPY my_table FROM STDIN CSV HEADER", f)

conn.commit()
cur.close()
conn.close()

print("ETL job completed successfully!")