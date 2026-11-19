from sqlalchemy import Column, Integer, String, Float, DateTime, CheckConstraint, func
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=True)
    department = Column(String(50), nullable=True)
    designation = Column(String(50), nullable=True)
    salary = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("salary >= 0", name="check_positive_salary"),
    )

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.full_name}', email='{self.email}')>"
