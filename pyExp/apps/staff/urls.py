from .controllers import post_json


def setup_routes(app):
    app.add_route(post_json, "/staff", methods=["POST"])
