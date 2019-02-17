from django.shortcuts import render, HttpResponse
from django.views import View
from django.core import serializers
# Create your views here.
from Music import models

class home(View):

    def get(self, request):
        return render(request, 'home.html')


class singer(View):

    def get(self, request, nid):
        singers = models.Singer.objects.filter(nid=nid)[0:15]
        return render(request, 'singer.html', {'singers': singers})

    def post(self, request, nid):
        a = int(request.POST.get('start', None))
        singers = models.Singer.objects.filter(nid=nid)[a:a+10]
        data = serializers.serialize("json", singers)
        return HttpResponse(data)


class detail(View):

    def get(self, request, sid):
        singer = models.Singer.objects.filter(id=sid).first()
        links = models.Info.objects.filter(sid=sid)
        info = {'singer': singer, 'links': links}
        return render(request, 'details.html', {'info': info})






