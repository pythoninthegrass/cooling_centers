from plain.http import Response
from plain.urls import Router, path

def index(request):
    return Response("Welcome to Cooling Centers - Plain framework is running!")

class AppRouter(Router):
    namespace = ""
    urls = [
        path("", index, name="index"),
    ]

urls = AppRouter