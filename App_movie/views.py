from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models.fields.files import ImageFieldFile
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files.images import ImageFile
from django.core.files import File
import json
import io

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

@method_decorator([csrf_exempt], name='dispatch')
class TestView(View):
    def get(self, request):
        mouvies = MovieModel.objects.all()
        fields = ['movieName', 'isAnnouced', 'movieCreation_date', 'movieImage']
        return JsonResponse(toDic(mouvies, fields), safe=False)
    
    def post(self, request):
        data1 = request.POST.get("movieName")
        data2 = request.POST.get("isAnnouced")
        data3 = request.POST.get("movieCreation_date")
        # data4 = request.FILES['movieImage'].read()

        # obj = MovieModel()
        # obj.movieName = data1
        # obj.isAnnouced = data2
        # obj.movieCreation_date = data3
        # obj.movieImage = ImageFile(io.BytesIO(data4), name='foo.jpg')
        # obj.save()
        #json_data = json.loads(request.body)
        print(data1)
        print(data2)
        print(data3)
        print("POST")
        #print(request.POST.get("movieName"))
        #print(data4.read())
        return HttpResponse("Success Post")
