from nameko.rpc import RpcProxy
from nameko.timer import timer
import random
import json

INTERVAL = 60
DATA_PATH = "data.json"


class Simulator(object):
    """
    A service that simulates ping request from the vehicles
    """
    name = "simulator"
    monitor = RpcProxy("monitor")

    def __init__(self):
        file = open(DATA_PATH, "r")
        self.ids = json.loads(file.read())
        self._send_ping()

    @timer(interval=INTERVAL)
    def send_ping(self):
        """
        recurring task to send ping as from vehicles
        """
        print("simulating", self.ids)
        self._send_ping()

    def _send_ping(self):
        """
        send ping according to a random choice will be done for every vehicle to decide if it will send or not
        :return:
        """
        if not self.ids:
            return
        for vehicle_id in self.ids:
            up = random.choice([True, False])
            if up:
                self.monitor.ping(vehicle_id)
