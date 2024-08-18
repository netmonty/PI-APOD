import requests
import psycopg2

def fetch_apod():
    API_URL = "https://api.nasa.gov/planetary/apod"
    API_KEY = "DEMO_KEY"
    params = {"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    return response.json()

def log_to_db(data):
    conn = psycopg2.connect("dbname=apod_db user=postgres password=password host=db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS apod_log (
            date TEXT PRIMARY KEY,
            title TEXT,
            url TEXT,
            explanation TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO apod_log (date, title, url, explanation)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (date) DO NOTHING
    ''', (data['date'], data['title'], data['url'], data['explanation']))

    conn.commit()
    cursor.close()
    conn.close()
