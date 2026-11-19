from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new employee"
)
def create_new_employee(
    employee_in: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    # Check for duplicate email
    existing_employee = crud.get_employee_by_email(db, email=employee_in.email)
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"An employee with email '{employee_in.email}' is already registered."
        )

    return crud.create_employee(db=db, employee_in=employee_in)


@router.get(
    "/",
    response_model=List[schemas.EmployeeResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all employees"
)
def read_all_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return crud.get_all_employees(db=db, skip=skip, limit=limit)


@router.get(
    "/search",
    response_model=List[schemas.EmployeeResponse],
    status_code=status.HTTP_200_OK,
    summary="Search employees"
)
def search_employees_by_query(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return crud.search_employees(db=db, search_query=q, skip=skip, limit=limit)


@router.get(
    "/{employee_id}",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Get employee details by ID"
)
def read_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    db_employee = crud.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )
    return db_employee


@router.put(
    "/{employee_id}",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Update employee information"
)
def update_existing_employee(
    employee_id: int,
    employee_update: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    # Verify employee exists
    db_employee = crud.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )

    # Check email collision with another employee
    if employee_update.email and employee_update.email != db_employee.email:
        email_owner = crud.get_employee_by_email(db, email=employee_update.email)
        if email_owner and email_owner.id != employee_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Email '{employee_update.email}' is already in use by another employee."
            )

    return crud.update_employee(
        db=db, 
        db_employee=db_employee, 
        employee_update=employee_update
    )


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an employee"
)
def delete_existing_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    db_employee = crud.get_employee_by_id(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found."
        )

    crud.delete_employee(db=db, db_employee=db_employee)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
