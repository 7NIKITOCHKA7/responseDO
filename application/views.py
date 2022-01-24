from django.http import HttpResponse
from django.shortcuts import render


def response204(request):
    return HttpResponse(status=204)

def response500(request):
    return HttpResponse(status=500)

def response200(request):
    return HttpResponse(status=200)
