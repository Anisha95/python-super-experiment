from backstack.controllers import BaseController
from backstack.mixins import ListMixin, ViewMixin, CreateMixin, UpdateMixin
from backstack.auth import owner_required, login_required
from backstack.db import db
from sqlalchemy.orm.exc import NoResultFound

from sanic import response
from .model import Staff
from .schema import StaffSchema


class StaffListController(BaseController, ListMixin, CreateMixin):
    model = Staff
    serializer_class = StaffSchema

    def handle_post(self, *args, **kwargs):
        return super().handle_post(*args, **kwargs)

    def handle_get(self, *args, **kwargs):
        return super().handle_get()
