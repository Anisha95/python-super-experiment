from base.controller import PyExBaseController
from .models import Staff
from .schema import StaffSchema
from backstack.mixins import CreateMixin


# def post_json(request):
#     return response.json({
#         "body": decode(request.body)
#     }, status=201
#     )


class StaffController(PyExBaseController, CreateMixin):
    model = Staff
    serializer_class = StaffSchema

    def handle_post(self, *args, **kwargs):
        return super().handle_post(*args, **kwargs)
