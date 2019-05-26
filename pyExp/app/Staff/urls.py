from .controller import post_json


def setup_routes(app):
    app.add_route(post_json.as_view(), "/staff", methods=["GET"])
