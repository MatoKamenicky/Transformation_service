from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import Transformation_service as ts



def web_transform(request):
    x, y, z = 123456, 789012, 100  # Example height in meters

    from_epsg = 5514
    to_epsg   = 4326
    result = ts.transform_coordinates(x, y, z, from_epsg, to_epsg)
    return render(request, 'result_template.html', {'result': result})

