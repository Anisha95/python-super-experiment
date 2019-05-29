from .controllers import StaffController


def setup_routes(app):
    app.add_route(StaffController.as_view(), "/staff", methods=["POST"])
