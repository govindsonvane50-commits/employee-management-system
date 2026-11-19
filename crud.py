from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_

import models
import schemas


def get_employee_by_id(db: Session, employee_id: int) -> Optional[models.Employee]:
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, email: str) -> Optional[models.Employee]:
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def get_all_employees(db: Session, skip: int = 0, limit: int = 100) -> List[models.Employee]:
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee_in: schemas.EmployeeCreate) -> models.Employee:
    db_employee = models.Employee(
        full_name=employee_in.full_name,
        email=employee_in.email,
        phone=employee_in.phone,
        department=employee_in.department,
        designation=employee_in.designation,
        salary=employee_in.salary,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(
    db: Session, 
    db_employee: models.Employee, 
    employee_update: schemas.EmployeeUpdate
) -> models.Employee:
    # Update only fields provided by client
    update_data = employee_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_employee, field, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, db_employee: models.Employee) -> None:
    db.delete(db_employee)
    db.commit()


def search_employees(
    db: Session, 
    search_query: str, 
    skip: int = 0, 
    limit: int = 100
) -> List[models.Employee]:
    # Case-insensitive search on name or email
    pattern = f"%{search_query}%"
    return (
        db.query(models.Employee)
        .filter(
            or_(
                models.Employee.full_name.ilike(pattern),
                models.Employee.email.ilike(pattern),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
