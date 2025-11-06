from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data")

def transform():
    print("Transforming data")

def load():
    print("Loading data")

with DAG('my_etl_pipeline', start_date=datetime(2025, 11, 6), schedule_interval='@daily') as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)

    t1 >> t2 >> t3  # Defines dependencies