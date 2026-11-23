from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.repositories import employee_repository


def create_employee(db: Session, employee_in: EmployeeCreate) -> Employee:
    # Check for duplicate email
    existing_employee = employee_repository.get_employee_by_email(db, email=employee_in.email)
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"An employee with email '{employee_in.email}' is already registered."
        )

    return employee_repository.create_employee(db=db, employee_in=employee_in)


def get_all_employees(db: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    return employee_repository.get_all_employees(db=db, skip=skip, limit=limit)


def get_employee_by_id(db: Session, employee_id: int) -> Employee:
    db_employee = employee_repository.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )
    return db_employee


def search_employees(db: Session, search_query: str, skip: int = 0, limit: int = 100) -> List[Employee]:
    return employee_repository.search_employees(db=db, search_query=search_query, skip=skip, limit=limit)


def update_employee(
    db: Session, 
    employee_id: int, 
    employee_update: EmployeeUpdate
) -> Employee:
    # Verify employee exists
    db_employee = employee_repository.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )

    # Check email collision with another employee
    if employee_update.email and employee_update.email != db_employee.email:
        email_owner = employee_repository.get_employee_by_email(db, email=employee_update.email)
        if email_owner and email_owner.id != employee_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Email '{employee_update.email}' is already in use by another employee."
            )

    return employee_repository.update_employee(
        db=db, 
        db_employee=db_employee, 
        employee_update=employee_update
    )


def delete_employee(db: Session, employee_id: int) -> None:
    db_employee = employee_repository.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )

    employee_repository.delete_employee(db=db, db_employee=db_employee)
