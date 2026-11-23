# Employee Management System – REST API

A production-grade RESTful API built with **FastAPI**, **SQLAlchemy ORM**, **Pydantic**, **Alembic**, and **MySQL**, organized into a clean, modular, industry-standard layered architecture.

---

## 🚀 Features

- **Add Employee:** Create new employee records with input validation.
- **Get All Employees:** Retrieve a paginated list of all employees.
- **Get Employee by ID:** Retrieve details of a specific employee.
- **Update Employee:** Partial or full update of employee details.
- **Delete Employee:** Remove an employee from the system.
- **Search Employees:** Case-insensitive search by name or email.
- **Data Validation & Constraints:** Enforced unique emails and non-negative salaries.
- **Database Migrations:** Schema versioning managed via Alembic.
- **Modular Architecture:** Clean separation across Core, Database, Models, Schemas, Repositories, Services, and Routers.
- **Interactive Documentation:** Auto-generated Swagger UI and ReDoc.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Database Driver:** PyMySQL
- **Data Validation:** Pydantic v2
- **Config Management:** python-dotenv

---

## 📁 Project Architecture

```text
employee-management-system/
│
├── alembic/
│   ├── versions/
│   │   └── 1416f7ea46ba_create_employees_table.py
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py                   # Environment & application settings
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py               # Engine, SessionLocal, Base & get_db
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── employee.py                 # SQLAlchemy ORM models
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── employee.py                 # Pydantic request & response schemas
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── employee_repository.py      # Database CRUD operations
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── employee_service.py         # Business logic & error handling
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── employee_router.py          # API endpoints & HTTP controllers
│   │
│   └── main.py                         # FastAPI application entry point
│
├── tests/
│   └── __init__.py
│
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/employee-management-system.git
cd employee-management-system
```

### 2. Create and activate a Virtual Environment
```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your MySQL credentials:
```ini
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_management_db
```

### 5. Run Database Migrations (Alembic)

```bash
# If your MySQL database already has the employees table:
alembic stamp head

# If setting up on a fresh/new database:
alembic upgrade head
```

### 6. Run the Application
```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation & Endpoints

Once the application is running, open your browser:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `POST` | `/employees/` | Add a new employee | `201 Created` |
| `GET` | `/employees/` | Get all employees (paginated) | `200 OK` |
| `GET` | `/employees/search?q={query}` | Search employees by name or email | `200 OK` |
| `GET` | `/employees/{employee_id}` | Get employee details by ID | `200 OK` |
| `PUT` | `/employees/{employee_id}` | Update employee information | `200 OK` |
| `DELETE` | `/employees/{employee_id}` | Delete an employee | `204 No Content` |
