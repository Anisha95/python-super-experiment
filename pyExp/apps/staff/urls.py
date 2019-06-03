from .controllers import StaffController, StaffListController


def setup_routes(app):
    app.add_route(StaffListController.as_view(), "/staff", methods=["GET", "POST"])
    app.add_route(StaffController.as_view(), "/staff/<id:int>/", methods=["PUT", "DELETE"])
