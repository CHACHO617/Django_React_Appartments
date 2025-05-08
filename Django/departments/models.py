from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
