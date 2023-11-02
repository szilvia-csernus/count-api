# count-api

> This simple Count API is created to count the page loads of some of my Frontend Applications to avoid overcharges.

Written in Python, using the FastAPI.

---

## Functionality

The API identifies the URLs where the request is coming from and if they come from from my approved sites, increments the count by one and returns the counter's state alongside a 200 status response. Otherwise it returns a status of 400, Bad Request.

The counter registers and always updates the last visit's date and resets the counter to 1 if it recognises a new month. This is to ensure that the monthly allowances of the counts will reset for a new month.

---

## Python Packages Used

`fastapi`, `uvicorn`, `databases`, `asyncpg`

---

## Local Development

0. Make sure python is installed.
1. create a virtual environment with `python3 -m venv venv`
2. activate the virtual environment: `source venv/bin/activate`
3. install the required packages: `pip install -r requirements.txt`

To run the server on a local development environment:

`uvicorn page_visits_app:app --reload`

---

## Deployment

The project is deployed on `AZURE`'s FaaS platform. The postgreSQL database is deployed on ElephantSQL.