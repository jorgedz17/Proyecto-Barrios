import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
"""
def damap(request):
    ctx = {
        'is_staff':request.user.is_staff,
        'username': request.user.username,
        'tdata': '/tdata/',
        'sdata': '/sdata/',
    }
    return render(request, 'p_risk_template.html', ctx)


def territorial_data(request):
    region = request.POST.get('region', 'Valparaiso')
    with open('RiskmapApp/data/data_UV17_valpo_010420.json', 'r') as fin:
        data = json.load(fin)
    return HttpResponse(json.dumps(data), content_type="application/json")


@login_required(login_url='/login/')
def sensitive_data(request):
    with open('RiskmapApp/data/pdata.json', 'r') as fin:
        data = json.load(fin)
    return HttpResponse(json.dumps(data), content_type="application/json")
"""
