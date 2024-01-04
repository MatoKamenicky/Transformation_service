from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import Transformation_service as ts
#from .forms import CoordinateForm
from .forms import CoordinateForm

"""
def web_transform(request):
    x, y, z = 123456, 789012, 100  # Example height in meters

    from_epsg = 5514
    to_epsg   = 4326
    result = ts.transform_coordinates(x, y, z, from_epsg, to_epsg)
    return render(request, 'button_template.html', {'result': result})
"""

def web_transform(request):
    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            x = int(form.cleaned_data['x_coordinate'])
            y = int(form.cleaned_data['y_coordinate'])
            z = 100

            from_epsg = 5514
            to_epsg   = 4326
            result = ts.transform_coordinates(x, y, z, from_epsg, to_epsg)
            print(result)
    else:
        form = CoordinateForm()
    return render(request, 'button_template.html', {'form': form})


def custom_404(request, exception):
    return render(request, 'C:/GAK/_ING_studium/ING_3_sem/web_gis/TransformacnaSluzba/web_app/templates/404.html', status=404)