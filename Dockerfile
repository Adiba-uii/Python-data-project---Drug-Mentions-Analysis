FROM apache/airflow:2.2.4-python3.8

COPY  --chown=airflow:root data/ .
COPY  --chown=airflow:root output/ .
COPY  --chown=airflow:root workflow/ .
COPY  --chown=airflow:root constants.py/ .
COPY  --chown=airflow:root main.py/ .

