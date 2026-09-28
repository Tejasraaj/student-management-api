# Student Management API

A lightweight RESTful CRUD API built with FastAPI and SQLite using SQLAlchemy and Pydantic.

## Features

- **Create Student**: `POST /students`
- **Get All Students**: `GET /students`
- **Get Student by ID**: `GET /students/{student_id}`
- **Update Student**: `PUT /students/{student_id}`
- **Delete Student**: `DELETE /students/{student_id}`
- **Search Students by Course**: `GET /students/search?course={course_name}`

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Open the interactive API documentation (Swagger UI):
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
