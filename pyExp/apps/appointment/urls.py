from .controllers import AppointmentListController, AppointmentController


def setup_routes(app):
    app.add_route(AppointmentListController.as_view(), "/appointments", methods=["OPTIONS", "GET", "POST"])
    app.add_route(AppointmentController.as_view(), "/appointments/<id:int>/", methods=["PUT", "DELETE"])
