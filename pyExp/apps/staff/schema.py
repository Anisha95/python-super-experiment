from backstack.schema import SystemSchema
from .models import Staff
from backstack import schema_fields as fields


class StaffSchema(SystemSchema):
    """
    Used to combine the whole staff
    """
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    dob = fields.Date(required=True)
    gender = fields.String(required=True)
    qualifications = fields.String(required=True)
    other_details = fields.String(required=True)

    class Meta:
        model = Staff
        fields = (
            "id", "first_name", "last_name", "dob", "gender", "qualifications", "other_details"
        )
