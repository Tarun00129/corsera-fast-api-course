# corsera-fast-api-course

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

To start the FastAPI server, run:

```bash
python -m uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/scalar`.
