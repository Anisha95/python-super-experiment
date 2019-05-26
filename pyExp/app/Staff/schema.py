from backstack.schema import BaseSchema
from .model import Staff
from backstack import schema_fields as fields


class StaffSchema(BaseSchema):
    """
    Used to combine the whole user Profile
    """
    first_name = fields.String()
    last_name = fields.String()
    dob = fields.Date()
    gender = fields.String()
    qualifications = fields.String()
    other_details = fields.String()

    class Meta:
        model = Staff
        fields = (
            "id", "first_name", "last_name", "dob", "gender", "qualifications",
            "other_details"
        )
