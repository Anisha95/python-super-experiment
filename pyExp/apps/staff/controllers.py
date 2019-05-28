from sanic import response
from ujson import decode


def post_json(request):
    return response.json({
        "body": decode(request.body)
    }, status=201
    )
