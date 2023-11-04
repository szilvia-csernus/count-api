# count-api

> This lightweight API is created to count the page loads of some of my Frontend Applications to be able to avoid overcharges.

Written in Python, using the FastAPI.

---

## Functionality

The API identifies the requests' URLs and if they are my approved sites, increments the count by one and returns the counter's state alongside a 200 status response. Otherwise it returns a status of 400, Bad Request.

The counter always updates the last visit's date and resets the counter to 1 if it recognises a new month. This is to ensure that the monthly allowances of the counts will reset if a new month is detected.

---

## Python Packages Used

`fastapi`, `uvicorn`, `pydantic`, `sqlalchemy`, `asyncpg`, `psycopg2-binary`, `psycopg2`, `databases`, `python-dotenv`

---

## Local Development

0. Make sure python is installed.
1. Create a virtual environment with `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install the required packages: `pip install -r requirements.txt`

To run the server on a local development server:

`uvicorn main:app --reload`

---

## Deployment

The project is deployed on `Heroku`, the postgreSQL database is deployed on `ElephantSQL`.