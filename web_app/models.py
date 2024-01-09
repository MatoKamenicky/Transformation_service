from django.db import models

class Coordinate(models.Model):
    x_coordinate = models.FloatField(default=None)
    y_coordinate = models.FloatField(default=None)
    z_coordinate = models.FloatField(null=True, default=None)
    result_x = models.DecimalField(max_digits=100, decimal_places=3, default=None)
    result_y = models.DecimalField(max_digits=100, decimal_places=3, default=None)
    result_z = models.DecimalField(max_digits=100, decimal_places=3, default=None, null=True)