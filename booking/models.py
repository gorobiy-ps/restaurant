from django.db import models
from django.contrib.postgres.fields import ArrayField


CHOISES = (
    ('rectangle','rectangle'),
    ('ellipse', 'ellipse')
)


class Table(models.Model):
    name = models.CharField(max_length=30, verbose_name='table "number"')
    seats = models.IntegerField(verbose_name='number of seats')
    length = models.IntegerField(verbose_name='Length as percentage of the Hall length')
    width = models.IntegerField(verbose_name='Width as percentage of the Hall width')
    shape = models.CharField(max_length=30, choices=CHOISES)
    position =  ArrayField(
        models.IntegerField(),
        verbose_name='Position as percentage of the Hall (ex: 30,60)'
    )

    def __str__(self):
        return self.shape + ' ' + self.name


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    username = models.CharField(max_length=30)
    email = models.EmailField()
