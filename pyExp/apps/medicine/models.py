from sqlalchemy import Column, String, REAL
from backstack.models import SystemModel


class Medication(SystemModel):
    __tablename__ = "medication"

    medication_unit_cost = Column(REAL)
    medication_name = Column(String(length=50), unique=True)
    medication_description = Column(String(length=100))
    other_details = Column(String(length=140))
