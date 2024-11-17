from Airflow.orchestrator import pipeline_populate_db

if __name__ == "__main__":
    pipeline_populate_db(
        url="https://en.wikipedia.org/wiki/Alan_Turing",
        name_dataset="demo_viva"
    )