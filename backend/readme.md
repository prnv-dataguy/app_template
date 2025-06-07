# FastAPI Backend

This backend service is built with **FastAPI** and loads page content from a YAML file (`page_content.yml`). It includes logging, a lifespan context manager, and is ready for development and deployment with Python virtual environments or Docker.

---

## Features

- Loads page content from a YAML file
- Logging for debugging and monitoring
- FastAPI lifespan context for startup/shutdown events
- Ready for local development and Docker deployment

---

## File Structure

```
backend/
│
├── main.py              # FastAPI application entry point
├── page_content.yml     # YAML file with page content
├── requirements.txt     # Python dependencies
└── ...                  # Other backend files
```

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo/backend
```

---

### 2. Using Python Virtual Environment

#### a. Create and activate a virtual environment

```sh
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

#### b. Install dependencies

```sh
pip install -r requirements.txt
```

#### c. Run the FastAPI app

```sh
uvicorn main:app --reload
```

- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### d. Debugging

- Use breakpoints in `main.py` with your IDE (e.g., VS Code).
- Check logs in the terminal for info and errors.

---

### 3. Using Docker

#### a. Build the Docker image

```sh
docker build -t fastapi-backend .
```

#### b. Run the Docker container

```sh
docker run -d -p 8000:8000 --name fastapi-backend fastapi-backend
```

- The API will be available at [http://localhost:8000](http://localhost:8000)

---

## Notes

- Ensure `page_content.yml` is present in the `backend` directory.
- Update `requirements.txt` if you add new dependencies.
- For production, consider using a production-ready ASGI server like `gunicorn` with `uvicorn.workers.UvicornWorker`.

---

## License

MIT License (add your license here)