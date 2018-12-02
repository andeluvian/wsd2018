from django.http import Http404, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json

from .models import Continent, Country


def continent_json(request, continent_code):

    try:
        dictContinent = Continent.objects.get(code=continent_code).countries.all()
        dictData = {}
        for country in dictContinent:
            dictData[country.code] = country.name

    except:
        raise Http404("Continent was not found")

    jsonData = json.dumps(dictData)

    if (request.GET.get("callback") == None):
        return HttpResponse(jsonData, "application/json")
    else:
        jsonData = request.GET.get("callback")+"(%s)" % jsonData

        return HttpResponse(jsonData, "application/javascript")




def country_json(request, continent_code, country_code):


    try:
        continent = Continent.objects.get(code= continent_code)
        dictCountry = continent.countries.get(code=country_code)
        dictData = {"population":dictCountry.population,"capital":dictCountry.capital,"area":dictCountry.area}
    except:
        raise Http404("Country was not found")
    if (request.GET.get("callback") == None):
        return HttpResponse(jsonData, "application/json")
    else:
        ''''jsonData = json.dumps(dictData)'''
        jsonData = request.GET.get("callback")+"(%s)" % jsonData

        return HttpResponse(jsonData, "application/json")
