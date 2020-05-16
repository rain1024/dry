from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_context():
    print("hello")


args = {
    "owner": "airflow",
    "start_date": datetime(2019, 5, 5)
}
dag = DAG(
    dag_id='test_operator',
    default_args=args)

run_this = PythonOperator(
    task_id='test_operator',
    python_callable=print_context,
    dag=dag
)