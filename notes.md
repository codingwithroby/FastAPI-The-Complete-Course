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
> Path parameters are request parameters that have been attached to a URL