from django.shortcuts import render
from django.views import View
from django_starter.apps.core.logger import get_logger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


LOGGER = get_logger()


class IndexView(View):
    logger = LOGGER

    def get(self, request):
        self.logger.debug("Debug message.")
        self.logger.info("Name: " + self.logger.name)
        self.logger.warn("Be careful!")
        self.logger.error("BE REALLY CAREFUL!")
        return render(request, "example/index.html", {"title": "Example App",})


class HelloView(APIView):
    """
    This can be tested with the following:

    http post http://127.0.0.1:8000/api/token/ username=admin password=admin

    and then use the resulting access token:
    
    http http://127.0.0.1:8000/hello/ "Authorization: Bearer <ACCESS_TOKEN>"

    Successful response looks like:

    HTTP/1.1 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Length: 27
    Content-Type: application/json
    Date: Wed, 02 Sep 2020 01:06:29 GMT
    Referrer-Policy: same-origin
    Server: WSGIServer/0.2 CPython/3.8.5
    Vary: Accept, Origin
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY

    {
        "message": "Hello, World!"
    }
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)


def show_error(request):
    try:
        num1 = 10.0
        num2 = 0.0
        amount = num1 / num2
    except Exception as err:
        LOGGER.exception(err)
    return render(request, "example/error.html", {})
