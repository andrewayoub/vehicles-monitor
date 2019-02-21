from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=31)
    reg_nr = models.CharField(max_length=15)
    owner = models.ForeignKey(Customer, related_name="vehicles", on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_id
