from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from aeroport_codes import models
def get_code(request, code):
    #return HttpResponse(code.upper() + ' = ' + models.code_rar.get(code.upper()))
    city = models.code_rar.get(code.upper(), 'Port Not Found')
    ctx = {
        'city': city
    }
    return render(request, template_name = 'code.html', context = ctx)
def home(request):
    homelist = []
    # for i in homelist:
    #     homelist.append(models.code_rar)
    codes_d = {
        'homelist': homelist
    }
    return render(request, template_name = 'homepage.html', context = codes_d)
