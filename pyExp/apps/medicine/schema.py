from backstack.schema import SystemSchema
from .models import Medication
from backstack import schema_fields as fields


class MedicationSchema(SystemSchema):
    """
    Used to combine the whole medication
    """
    medication_unit_cost = fields.Decimal(required=True)
    medication_name = fields.String(required=True)
    medication_description = fields.String(required=True)
    other_details = fields.String(required=False)

    class Meta:
        model = Medication
        fields = (
            "id", "medication_unit_cost", "medication_name", "medication_description", "other_details"
        )
