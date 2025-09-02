# Person-CRUD-API-with-FastAPI-PostgreSQL-and-Alembic
📌 Overview
This project is a CRUD API (Create, Read, Update, Delete) built using:
FastAPI as the web framework
PostgreSQL as the database
SQLAlchemy ORM for defining models
Alembic for database migrations

The API allows you to manage Person records (with fields like id, name, email) and interact with a live PostgreSQL database. It also comes with interactive API documentation via Swagger UI (/docs) and ReDoc (/redoc).

This README will guide you through the complete setup — from environment creation to database migrations and API usage — so even beginners can run this project successfully.

🚀 Features
Add new persons with name and email.
Retrieve all persons from the database.
Retrieve a single person by ID.
Update a person’s details.
Delete a person.
Database version control using Alembic migrations.
Interactive API docs with Swagger (/docs).

🛠️ Tech Stack
Python 3.10+
FastAPI
Uvicorn (ASGI server)
SQLAlchemy
Alembic (for migrations)
PostgreSQL

⚙️ Setup Instructions
Create and activate virtual environment
On Windows (PowerShell):
python -m venv .venv
.venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
If requirements.txt doesn’t exist, manually install:
pip install fastapi uvicorn sqlalchemy psycopg2 alembic pydantic
🗄️ Database Setup
1️⃣ Create a PostgreSQL database
Open pgAdmin4 or use psql:
CREATE DATABASE person_db;
2️⃣ Update connection URL
In main.py (or database.py if separated), update:
DATABASE_URL = "postgresql+psycopg2://username:password@localhost/person_db"
Replace username, password, and person_db with your values.
🔄 Alembic Migrations
1️⃣ Initialize Alembic (only once)
alembic init alembic
2️⃣ Generate migration script
alembic revision --autogenerate -m "create persons table"
3️⃣ Apply migration
alembic upgrade head
Now the persons table is created inside your database 🎉
▶️ Run the Application
Start the FastAPI app with Uvicorn:
uvicorn main:app --reload
Output should look like:
INFO:     Uvicorn running on http://127.0.0.1:8000
📖 API Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Both provide interactive documentation to test the API directly from the browser.

📌 Example API Usage
1️⃣ Create a Person
POST /persons/
{
  "name": "Sameer",
  "email": "sameer@example.com"
}

Response:

{
  "id": 1,
  "name": "Sameer",
  "email": "sameer@example.com"
}

2️⃣ Get All Persons

GET /persons/

[
  {
    "id": 1,
    "name": "Sameer",
    "email": "sameer@example.com"
  }
]

3️⃣ Get Person by ID

GET /persons/1

{
  "id": 1,
  "name": "Sameer",
  "email": "sameer@example.com"
}

4️⃣ Update a Person

PUT /persons/1

{
  "name": "Sameer Khan",
  "email": "sameer.khan@example.com"
}

5️⃣ Delete a Person

DELETE /persons/1

Response:

{
  "message": "Person deleted successfully"
}

📊 Verify in PostgreSQL (pgAdmin4)
Run in pgAdmin Query Tool:

SELECT * FROM persons;


Output:

 id |   name   |        email
----+----------+----------------------
  1 | Sameer   | sameer@example.com

And load with python-dotenv.

✅ Learning Outcomes
By completing this project, I have learned:
How to set up FastAPI
How to use SQLAlchemy ORM models
How to apply Alembic migrations
How to connect FastAPI to PostgreSQL
How to test APIs with Swagger UI & pgAdmin4
