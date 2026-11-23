from typing import List
from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.database.connection import get_db
from app.services import employee_service

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new employee"
)
def create_new_employee(
    employee_in: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return employee_service.create_employee(db=db, employee_in=employee_in)


@router.get(
    "/",
    response_model=List[EmployeeResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all employees"
)
def read_all_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return employee_service.get_all_employees(db=db, skip=skip, limit=limit)


@router.get(
    "/search",
    response_model=List[EmployeeResponse],
    status_code=status.HTTP_200_OK,
    summary="Search employees"
)
def search_employees_by_query(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return employee_service.search_employees(db=db, search_query=q, skip=skip, limit=limit)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Get employee details by ID"
)
def read_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return employee_service.get_employee_by_id(db=db, employee_id=employee_id)


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Update employee information"
)
def update_existing_employee(
    employee_id: int,
    employee_update: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return employee_service.update_employee(
        db=db, 
        employee_id=employee_id, 
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
    employee_service.delete_employee(db=db, employee_id=employee_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
