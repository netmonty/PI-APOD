from dagster import op, job, schedule
from apod_app import fetch_apod, log_to_db

@op
def fetch_apod_op():
    return fetch_apod()

@op
def log_to_db_op(data):
    log_to_db(data)

@job
def apod_pipeline():
    data = fetch_apod_op()
    log_to_db_op(data)

@schedule(cron_schedule="0 0 * * *", job=apod_pipeline)
def daily_apod_schedule():
    return {}
