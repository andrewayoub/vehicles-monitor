# Monitoring service
We can call this the core component as it's actually the service responsible for monitoring vehicles.

# This service uses
* [Nameko](https://nameko.readthedocs.io/en/stable/) microservices framework
* [RabbitMQ](https://www.rabbitmq.com/) message broker
* [Redis](https://redis.io/) in-memory database

## How to run:
```bash
cd {vehicles-monitor repo dir}/website
pipenv shell
nameko run monitor --broker amqp://guest:guest@rabbitmq:5672
```

# How it works
when this service runs it has two methods which can be called using Nameko:  
    1- ping(vehicle_id): this is the method which should be use by the vehicle to send a ping when this method is called 
    it writes to a HSET in redis db where the key is the vehicle_id and the value is the current time stamp.  
    2- get_vehicles_status(): retrieves the status of each machine has ever binged in a dict (True = Alive, Flase =
     Dead) it decides whether the vehicle is up or not by comparing the current time with the stored timestamp.
     
     
