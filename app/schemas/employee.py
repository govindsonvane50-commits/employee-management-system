from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class EmployeeBase(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    department: Optional[str] = Field(None, max_length=50)
    designation: Optional[str] = Field(None, max_length=50)
    salary: float = Field(..., ge=0, description="Salary must be non-negative")


class EmployeeCreate(EmployeeBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "full_name": "Govinda Sharma",
                "email": "govinda@example.com",
                "phone": "+91 9876543210",
                "department": "Engineering",
                "designation": "Python Backend Developer",
                "salary": 75000.00
            }
        }
    )


class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    department: Optional[str] = Field(None, max_length=50)
    designation: Optional[str] = Field(None, max_length=50)
    salary: Optional[float] = Field(None, ge=0)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "full_name": "Govinda Sharma",
                "email": "govinda.new@example.com",
                "phone": "+91 9876500000",
                "department": "Engineering",
                "designation": "Senior Python Backend Developer",
                "salary": 90000.00
            }
        }
    )


class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "full_name": "Govinda Sharma",
                "email": "govinda@example.com",
                "phone": "+91 9876543210",
                "department": "Engineering",
                "designation": "Python Backend Developer",
                "salary": 75000.00,
                "created_at": "2026-11-19T00:00:00Z",
                "updated_at": "2026-11-19T00:00:00Z"
            }
        }
    )
