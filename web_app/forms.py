from django import forms
from .models import Coordinate

class CoordinateForm_xy(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['x_coordinate', 'y_coordinate']

class CoordinateForm_xyz(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['x_coordinate', 'y_coordinate', 'z_coordinate']