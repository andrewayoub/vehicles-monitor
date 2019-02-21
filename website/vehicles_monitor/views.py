from django.http import HttpResponse
from django.shortcuts import render
from .models import Vehicle
import json
from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}

def index(request):
    return render(request, "index.html")


def vehicles(request):
    if request.method == 'GET':
        with ClusterRpcProxy(CONFIG) as rpc:
            vehicles = Vehicle.objects.all()
            statuses = rpc.monitor.get_vehicles_status()
            results = list()
            for vehicle in vehicles:
                result = {
                    "id": vehicle.vehicle_id,
                    "reg_nr": vehicle.reg_nr,
                    "owner_name": vehicle.owner.name,
                    "owner_address": vehicle.owner.address,
                    "up": vehicle.vehicle_id in statuses and statuses[vehicle.vehicle_id]
                }
                results.append(result)
            return HttpResponse(json.dumps(results))
