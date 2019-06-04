from backstack.schema import SystemSchema
from .models import Patient
from backstack import schema_fields as fields


class PatientSchema(SystemSchema):
    """
    Used to combine the whole patient
    """
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    dob = fields.Date(required=True)
    gender = fields.String(required=True)
    other_details = fields.String(required=True)

    class Meta:
        model = Patient
        fields = (
            "id", "first_name", "last_name", "dob", "gender", "other_details"
        )
