from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cities(request):
    return HttpResponse('Hello Belarus')