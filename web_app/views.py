from django.shortcuts import render, redirect
from . import Transformation_service as ts
from .forms import CoordinateForm
from .models import Coordinate

def home(request):
    return render(request, 'home.html')

def transform_xy(request):
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
    return render(request, 'transform_xy.html', {'form': form})

def transform_xyz(request):
    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            x = int(form.cleaned_data['x_coordinate'])
            y = int(form.cleaned_data['y_coordinate'])
            z = int(form.cleaned_data['z_coordinate'])

            from_epsg = 5514
            to_epsg   = 4326
            result = ts.transform_coordinates(x, y, z, from_epsg, to_epsg)
            Coordinate.objects.create(x_coordinate=x, y_coordinate=y, result_x=result[0], result_y=result[1], result_z=result[2])
            return redirect('result')
    else:
        form = CoordinateForm()
    return render(request, 'transform_xyz.html', {'form': form})

def about_us(request):
    return render(request, 'about_us.html')

def result(request):
    latest_calculation = Coordinate.objects.last()
    result_string = f"{latest_calculation.result_x} {latest_calculation.result_y} {latest_calculation.result_z}"
    return render(request, 'result.html', {'result_string': result_string})

def custom_404(request, exception):
    return render(request, 'C:/GAK/_ING_studium/ING_3_sem/web_gis/TransformacnaSluzba/web_app/templates/404.html', status=404)