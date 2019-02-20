from nameko.rpc import rpc
from redis import Redis
from time import time

HSET_NAME = "monitoring"
TTL = 60


class Monitor(object):
    """
    The monitoring service, it uses a redis server to store vehicles ping data in a HSET, currently it's hardcoded to
    use a local redis server on port 6379
    """
    name = "monitor"

    def __init__(self):
        self.redis_connection = Redis(host="localhost", port=6379)

    @rpc
    def ping(self, vehicle_id):
        """
        a method is to be used by the vehicles or the simulator to ping, in other words send I'm alive message
        :param vehicle_id: the vehicle id
        :return: None
        """
        self.redis_connection.hset(HSET_NAME, vehicle_id, time())

    @rpc
    def get_vehicles_status(self):
        """
        gets the status of the vehicles, a vehicle is alive if it has pinged in the last TTL seconde (TTL=60)
        :return: a dict {"vehicle_id" : `True if the vehicle is alive other wise false`}
        """
        vehicles_data = self.redis_connection.hgetall(HSET_NAME)
        result = dict()
        now = time()
        for key, value in vehicles_data.items():
            if float(value) + TTL > now:
                result[key.decode()] = True
            else:
                result[key.decode()] = False
        return result
