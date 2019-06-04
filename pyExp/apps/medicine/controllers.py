from base.controller import PyExBaseController
from .models import Medication
from .schema import MedicationSchema
from sqlalchemy.orm.exc import NoResultFound
from backstack.db import db
from sanic import response
from backstack.mixins import CreateMixin, ListMixin, UpdateMixin, ViewMixin


# def post_json(request):
#     return response.json({
#         "body": decode(request.body)
#     }, status=201
#     )
class MedicationListController(PyExBaseController, ListMixin, CreateMixin):
    model = Medication
    serializer_class = MedicationSchema


class MedicationController(PyExBaseController, ListMixin, ViewMixin, UpdateMixin):
    model = Medication
    serializer_class = MedicationSchema
    url_parts = {
        "id": Medication.id,
        "url": Medication.__tablename__,
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

            content_list = Medication.query().filter(Medication.url.ilike("{}%".format(self.kwargs["url"]))).all()
            return response.json(
                self.get_serializer().dump(content_list, many=True).data
            )

    def handle_delete(self, *args, **kwargs):
        db.session.delete(self.get_item())
        db.session.commit()
        return response.json({
            "message": "removed successfully."
        }, status=202)
