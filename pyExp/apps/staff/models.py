from sqlalchemy import Column, String, Date
from backstack.models import SystemModel


class Staff(SystemModel):
    __tablename__ = "staff"

    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(String(length=1), nullable=False)
    qualifications = Column(String(length=100), nullable=False)
    other_details = Column(String(length=140), nullable=True)
