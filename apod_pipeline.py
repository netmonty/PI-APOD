from dagster import schedule, job, op
import requests
import sqlite3

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"  # Replace with your NASA API key if you're using other API calls to NASA


@op
def fetch_apod():
    params = {"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data


@op
def log_to_db(data):
    # Connect to SQLite database (path within Docker container)
    conn = sqlite3.connect('/app/apod.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS apod_log (
            date TEXT PRIMARY KEY,
            title TEXT,
            url TEXT,
            explanation TEXT
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT OR REPLACE INTO apod_log (date, title, url, explanation)
        VALUES (?, ?, ?, ?)
    ''', (data['date'], data['title'], data['url'], data['explanation']))

    conn.commit()
    conn.close()


@job
def apod_pipeline():
    log_to_db(fetch_apod())


# Schedule the job to run daily at midnight UTC
@schedule(cron_schedule="0 0 * * *", job=apod_pipeline)
def daily_apod_schedule():
    return {}

