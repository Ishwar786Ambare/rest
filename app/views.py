from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from app.models import Emp
from app.serilizers import EmpSeri


def index(request):
    pass


def about(request):
    pass


def my_view(request): pass


class MainPage(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            emp = Emp.objects.get(id=id)
            emps = EmpSeri(emp)
            json_data = JSONRenderer().render(emps.data)
            return HttpResponse(json_data, content_type='application/json')

        emp = Emp.objects.all()
        emps = EmpSeri(emp, many=True)
        json_data = JSONRenderer().render(emps.data)
        return HttpResponse(json_data, content_type='application/json')
