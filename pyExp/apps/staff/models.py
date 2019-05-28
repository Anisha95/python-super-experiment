from sqlalchemy import Column, String, Date, Integer
from backstack.models import SystemModel


class Staff(SystemModel):
    __tablename__ = "staff"

    Column("first_name", String(32), unique=True, nullable=False)
    Column("last_name", String(32), unique=True, nullable=False)
    Column("dob", Date, nullable=False)
    Column("gender", String(length=1), nullable=False)
    Column("qualifications", String(length=100), nullable=False)
    Column("other_details", String(length=140), nullable=True)

