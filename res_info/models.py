from django.db import models


# Create your models here.

class GeneralInformation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{} {} {}".format(self.name, self.address, self.city)
