from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import Transformation_service as ts
from .forms import CoordinateForm
from .models import Coordinate

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
            Coordinate.objects.create(x_coordinate=x, y_coordinate=y, result_x=result[0], result_y=result[1], result_z=result[2])
            return redirect('result')
    else:
        form = CoordinateForm()
    return render(request, 'button_template.html', {'form': form})

def result(request):
    latest_calculation = Coordinate.objects.last()
    result_string = f"{latest_calculation.result_x} {latest_calculation.result_y} {latest_calculation.result_z}"
    return render(request, 'result.html', {'result_string': result_string})

def custom_404(request, exception):
    return render(request, 'C:/GAK/_ING_studium/ING_3_sem/web_gis/TransformacnaSluzba/web_app/templates/404.html', status=404)