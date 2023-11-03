from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from datetime import date
import databases
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
database = databases.Database(os.getenv('DATABASE_URL'))


@app.get("/visit/{page_name}")
async def increment_page_visit(page_name: str, request: Request):
    # Extract the URL from the request headers
    request_url = str(request.url)
    current_date = date.today()

    # Check if the request URL matches the specified page_name
    if request_url == page_name:
        # Query to fetch the count and last_visit for the specified page_name
        query = "SELECT count, last_visit FROM page_visits \
                WHERE page_name = :page_name"
        values = {"page_name": page_name}

        # Execute the query
        result = await database.fetch_one(query=query, values=values)

        if result:
            last_visit = result['last_visit']
            last_visit_month = last_visit.month
            current_month = current_date.month

            if last_visit_month != current_month:
                # If the last visit was in a different month, reset the count
                query = "UPDATE page_visits SET count = 1, \
                    last_visit = :current_date \
                    WHERE page_name = :page_name RETURNING count, last_visit"
            else:
                # Otherwise, increment the count and update the last_visit
                query = "UPDATE page_visits \
                    SET count = count + 1, \
                    last_visit = :current_date \
                    WHERE page_name = :page_name RETURNING count, last_visit"

            # Update the count and last_visit in the database
            values = {"page_name": page_name, "current_date": current_date}
            updated_result = await database.fetch_one(query=query,
                                                      values=values)

            if updated_result:
                updated_count = updated_result['count']
                last_visit = updated_result['last_visit']
                return JSONResponse(content={"count": updated_count,
                                             "last_visit": last_visit},
                                    status_code=200)
            else:
                return JSONResponse(
                    content={"message": "Page not found in database"},
                    status_code=404)
        else:
            return JSONResponse(
                content={"message": "Page not found in database"},
                status_code=404)
    else:
        return HTMLResponse(
            content="Request URL does not match the specified page_name",
            status_code=400)
