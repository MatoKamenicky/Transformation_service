from django.db import models

class Coordinate(models.Model):
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()