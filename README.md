# PI-APOD
Containerised API called to NASA's Astronomy Picture of the Day. Designed for RaspberryPi

This project schedules daily queries to NASA's Astronomy Picture of the Day (APOD) API, logs the responses to a SQLite database, and displays the image.

Dagster is utilised for pipeline orchestration (https://dagster.io/).
## Prerequisites
- Docker
- Docker Compose
- If you're using multiple instances or have other projects calling to US fed agencies use your own NASA API Key (get it from https://api.nasa.gov/#signUp)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/PI-APOD.git
   cd PI-APOD
2. Build Docker containers
   ```bash
   docker compose build
   docker compose up
   