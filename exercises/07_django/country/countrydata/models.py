from django.db import models


class Continent(models.Model):

    name = models.CharField(max_length=200,unique=True)
    code = models.CharField(max_length=2,unique=True)
    id = models.AutoField(primary_key=True)
    pass
    class Meta:
        ordering = ['name']

class Country(models.Model):

    name = models.CharField(max_length=200,unique=True)
    capital = models.CharField(max_length=200)
    code = code = models.CharField(max_length=2,unique=True)
    population = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,related_name='countries')
    pass
    class Meta:
        ordering = ['name']
