from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models.fields.files import ImageFieldFile

#Models
from .models import (
    MovieModel
)

def toDic(objs, fields):
    res = []
    for obj in objs:
        dictObj = {}
        for item in fields:
            f = getattr(obj, item)
            if isinstance(f, ImageFieldFile):
                dictObj[item] = f.name
            else:
                dictObj[item] = f
        res.append(dictObj)
    return res

class TestView(View):
    def get(self, request):
        mouvies = MovieModel.objects.all()
        fields = ['movieName', 'isAnnouced', 'movieCreation_date', 'movieImage']
        return JsonResponse(toDic(mouvies, fields), safe=False)
