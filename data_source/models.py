from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name