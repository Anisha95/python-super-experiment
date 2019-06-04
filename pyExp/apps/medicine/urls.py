from .controllers import MedicationListController, MedicationController


def setup_routes(app):
    app.add_route(MedicationListController.as_view(), "/medication", methods=["OPTIONS", "GET", "POST"])
    app.add_route(MedicationController.as_view(), "/medication/<id:int>/", methods=["PUT", "DELETE"])
