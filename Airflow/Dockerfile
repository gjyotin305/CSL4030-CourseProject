FROM python:3.10-slim

RUN pip install apache-airflow[postgres] pandas tiktoken

RUN airflow db init

RUN airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

CMD ["airflow", "webserver"]