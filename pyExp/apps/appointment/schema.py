from backstack.schema import SystemSchema
from .models import Appointment
from backstack import schema_fields as fields


class AppointmentSchema(SystemSchema):
    """
    Used to combine the whole appointment
    """
    patient_id = fields.Integer(required=True)
    staff_id = fields.Integer(required=True)
    date_time_of_appointment = fields.DateTime(required=True)
    other_details = fields.String(required=False)

    class Meta:
        model = Appointment
        fields = (
            "id", "patient_id", "staff_id", "date_time_of_appointment", "other_details"
        )
