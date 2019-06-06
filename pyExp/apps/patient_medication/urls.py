from .controllers import PatientMedicationListController, PatientMedicationController


def setup_routes(app):
    app.add_route(PatientMedicationListController.as_view(), "/patient-medication", methods=["OPTIONS", "GET", "POST"])
    app.add_route(PatientMedicationController.as_view(), "/patient-medication/<id:int>/", methods=["PUT", "DELETE"])
