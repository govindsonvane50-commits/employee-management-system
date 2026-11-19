# Employee Management System – REST API

A production-grade RESTful API built with **FastAPI**, **SQLAlchemy ORM**, **Pydantic**, and **MySQL**.

---

## 🚀 Features

- **Add Employee:** Create new employee records with input validation.
- **Get All Employees:** Retrieve a paginated list of all employees.
- **Get Employee by ID:** Retrieve details of a specific employee.
- **Update Employee:** Partial or full update of employee details.
- **Delete Employee:** Remove an employee from the system.
- **Search Employees:** Case-insensitive search by name or email.
- **Data Validation & Constraints:** Enforced unique emails and non-negative salaries.
- **Interactive Documentation:** Auto-generated Swagger UI and ReDoc.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Database Driver:** PyMySQL
- **Data Validation:** Pydantic v2
- **Config Management:** python-dotenv

---

## 📁 Project Architecture

```text
employee-management-system/
│
├── .env                  # Database credentials (excluded from git)
├── .env.example          # Template for required environment variables
├── .gitignore            # Git ignore file
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
├── database.py           # Database engine, SessionLocal, and get_db dependency
├── models.py             # SQLAlchemy ORM models (Employee table)
├── schemas.py            # Pydantic schemas for request/response validation
├── crud.py               # Pure database operations (CRUD & Search)
├── main.py               # FastAPI application entry point
│
└── routers/
    ├── __init__.py       # Package marker
    └── employees.py      # REST API route handlers
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
Copy `.env.example` to `.env`:
```ini
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_management_db
```

### 5. Create the MySQL Database
```sql
CREATE DATABASE IF NOT EXISTS employee_management_db;
```

### 6. Run the Application
```bash
uvicorn main:app --reload
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
