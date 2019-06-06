from base.controller import PyExBaseController
from .models import PatientMedication
from .schema import PatientMedicationSchema
from sqlalchemy.orm.exc import NoResultFound
from backstack.db import db
from sanic import response
from backstack.mixins import CreateMixin, ListMixin, UpdateMixin, ViewMixin


# def post_json(request):
#     return response.json({
#         "body": decode(request.body)
#     }, status=201
#     )
class PatientMedicationListController(PyExBaseController, ListMixin, CreateMixin):
    model = PatientMedication
    serializer_class = PatientMedicationSchema


class PatientMedicationController(PyExBaseController, ListMixin, ViewMixin, UpdateMixin):
    model = PatientMedication
    serializer_class = PatientMedicationSchema
    url_parts = {
        "id": PatientMedication.id,
        "url": PatientMedication.__tablename__,
    }

    def handle_get(self, *args, **kwargs):
        if "url" in self.kwargs:
            if self.kwargs["url"][0] == "/":
                self.kwargs["url"] = self.kwargs["url"][1:]
            if self.kwargs["url"][-1:] == "/":
                self.kwargs["url"] = self.kwargs["url"][:-1]
        try:
            self.get_item()
            return super().handle_get()
        except NoResultFound:

            content_list = PatientMedication.query().filter(PatientMedication.url.ilike("{}%".format(self.kwargs["url"]))).all()
            return response.json(
                self.get_serializer().dump(content_list, many=True).data
            )

    def handle_delete(self, *args, **kwargs):
        db.session.delete(self.get_item())
        db.session.commit()
        return response.json({
            "message": "removed successfully."
        }, status=202)
