from django.test import TestCase
from django.test.client import RequestFactory
from .models import Vehicle, Customer
from .views import vehicles
import mock
import json


class VehiclesApiTest(TestCase):

    @mock.patch('vehicles_monitor.views.ClusterRpcProxy')
    def test_vehicles_list(self, fakerpc):
        c = Customer(name="test_customer", address="test_address")
        c.save()
        v = Vehicle(vehicle_id="test_id", reg_nr="test_nr", owner=c)
        v.save()
        request = RequestFactory().get('/vehicles/')
        response = vehicles(request).content.decode()
        response = json.loads(response)
        assert len(response) == 1
        assert response[0]["id"] == v.vehicle_id
        assert response[0]["owner_name"] == v.owner.name
        assert response[0]['up'] is False

