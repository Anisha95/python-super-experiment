from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from backstack.models import SystemModel


class PatientMedication(SystemModel):
    __tablename__ = "patients_medication"

    medication_id = Column(Integer, ForeignKey("medication.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
    date_time_administered = Column(DateTime)
    dosage = Column(Integer, nullable=True)
    comments = Column(String(length=100), nullable=True)
    other_details = Column(String(length=140), nullable=True)
