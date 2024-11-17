from Airflow.orchestrator import pipeline_populate_db

if __name__ == "__main__":
    pipeline_populate_db(
        url="https://pastebin.com/raw/N3HCnu7m",
        name_dataset="demo_viva_1"
    )