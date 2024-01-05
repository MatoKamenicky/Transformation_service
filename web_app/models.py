from django.db import models

class Coordinate(models.Model):
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    result_x = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    result_y = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    result_z = models.DecimalField(max_digits=100, decimal_places=3, default=0)