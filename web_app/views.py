from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import Transformation_service



def web_transform(request):
    template = loader.get_template('template_try.html')
    return HttpResponse(template.render())
