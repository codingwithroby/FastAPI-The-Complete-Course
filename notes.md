# Introduction

## 1. Run a fastapi application:
```python
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

or

```python
pip install "fastapi[standard]"

# To run in development mode
fastapi dev main.py

# To run in production mode
fastapi run main.py
```

## 2. Path Parameters:
- Path parameters are request parameters that have been attached to a URL

## 3. Pydantics:
- Python library which is used for data validation/ data modeling/ data parsing/ error handling
- How to handle data coming to out FastAPI application

## 4. Status Codes:
- An HTTP status code is used to help the Client (the user or system submitting data to the server) to understand what happened on the server side application.
- International standards on how a Client/ Server should handle the result of request.
- It allows everyone who sends a request if the submittion was successful of not.
- Types:
    - 1xx - Information Response: Request Processing.
    - 2xx - Success: Requests successfully complete.
    - 3xx - Redirection: Further action must be complete.
    - 4xx - Client Errors: An error was caused by client.
    - 5xx - Server Errors: An error occurred on the server.

## 5. Sqlite
```sql
-- to enter into sqlite
sqlite3 

-- to view the schema of the database
.schema 

-- to change the table view mode
.mode [column, table, markdown, etc.]
```