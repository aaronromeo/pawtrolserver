from django.contrib.gis.db import models


class Badge(models.Model):
    '''
    Model to store Badge specific information

    '''
    name = models.CharField(max_length=255)
