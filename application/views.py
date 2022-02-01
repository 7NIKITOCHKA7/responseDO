from django.http import HttpResponse
from application.external import process_request, CustomException


def response204(request):
    return HttpResponse(status=204)


def response500(request):
    return HttpResponse(status=500)


def response200(request):
    return HttpResponse(status=200)


def response204_exc(request):
    try:
        process_request()
    except CustomException as exc:
        return exc.response()
