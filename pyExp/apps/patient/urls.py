from .controllers import PatientListController, PatientController


def setup_routes(app):
    app.add_route(PatientListController.as_view(), "/patient", methods=["OPTIONS", "GET", "POST"])
    app.add_route(PatientController.as_view(), "/patient/<id:int>/", methods=["PUT", "DELETE"])
