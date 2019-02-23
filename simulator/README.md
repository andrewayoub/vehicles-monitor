# Simulator service
An optional service to send fake status to the monitoring service

## This service uses
* [Nameko](https://nameko.readthedocs.io/en/stable/) microservices framework
* [RabbitMQ](https://www.rabbitmq.com/) message broker

## How to run:
```bash
cd {vehicles-monitor repo dir}/website
pipenv shell
nameko run simulator --broker amqp://guest:guest@rabbitmq:5672
```

## Description
when this service starts it will read the fake vehicles ids from `data.json` and each minute it will send a fake status 
for each one