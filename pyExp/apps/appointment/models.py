from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from backstack.models import SystemModel


class Appointment(SystemModel):
    __tablename__ = "appointments"

    patient_id = Column(Integer, ForeignKey("patient.id"))
    staff_id = Column(Integer, ForeignKey("staff.id"))
    date_time_of_appointment = Column(DateTime)
    other_details = Column(String(length=140), nullable=True)
