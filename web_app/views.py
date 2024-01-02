from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import Transformation_service as ts
import subprocess

"""
def web_transform(request):
    try:
        result = subprocess.run(["python", "myapp/scripts/myscript.py"], check=True, capture_output=True)
        output = result.stdout.decode('utf-8')
        return HttpResponse(f"Script executed successfully. Output:\n\n{output}")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Error executing script: {e}")

"""
def web_transform(request):
    x, y, z = 123456, 789012, 100  # Example height in meters

    from_epsg = 5514
    to_epsg   = 4326
    result = ts.transform_coordinates(x, y, z, from_epsg, to_epsg)
    return render(request, 'button_template.html', {'result': result})

def custom_404(request, exception):
    return render(request, 'C:/GAK/_ING_studium/ING_3_sem/web_gis/TransformacnaSluzba/web_app/templates/404.html', status=404)