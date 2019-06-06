from backstack.schema import SystemSchema
from .models import PatientMedication
from backstack import schema_fields as fields


class PatientMedicationSchema(SystemSchema):
    """
    Used to combine the whole medication
    """
    medication_id = fields.Integer(required=True)
    patient_id = fields.Integer(required=True)
    date_time_administered = fields.DateTime(required=True)
    dosage = fields.Integer(required=False)
    comments = fields.String(required=False)
    other_details = fields.String(required=False)

    class Meta:
        model = PatientMedication
        fields = (
            "id", "medication_id", "patient_id", "date_time_administered", "dosage", "comments", "other_details"
        )
