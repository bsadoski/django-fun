from django.shortcuts import render
from django.http import HttpResponse
from example.models import Reporter

# Create your views here.

def reporteres(request):
    rs = Reporter.objects.all().count()
    html = "<html><p> %i </p></html>" % rs
    return HttpResponse(html)

def reporter(request, id=1):
    rs = Reporter.objects.all()[id]
    html = "<html><p> %s </p></html>" % rs.first_name
    return HttpResponse(html)