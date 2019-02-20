from nameko.rpc import RpcProxy
from nameko.timer import timer
import random

INTERVAL = 60


class Simulator(object):
    """
    A service that simulates ping request from the vehicles
    """
    name = "simulator"
    monitor = RpcProxy("monitor")

    def __init__(self):
        # TODO: load the correct ids from config file
        self.ids = [1, 2, 3, 4, 5, 6]

    @timer(interval=INTERVAL)
    def send_ping(self):
        """
        recurring task to send ping as from vehicles, a random choice will be done for every vehicle to decide if it
        will send or not
        """
        print("simulating", self.ids)
        if not self.ids:
            return
        for vehicle_id in self.ids:
            up = random.choice([True, False])
            if up:
                self.monitor.ping(vehicle_id)
