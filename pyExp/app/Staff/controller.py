from backstack.controllers import BaseController
from backstack.config import settings
from backstack.errors import Errors
from backstack.mixins import ListMixin, CreateMixin
from backstack.db import db
from sqlalchemy.orm.exc import NoResultFound
from sanic import response
from .model import Staff
from .schema import StaffSchema


def post_json(request):
    return response.json({"received": True, "message": request.json})


