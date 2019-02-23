#Website Service
This is the customer facing component, it serves the ui and the api used for it.

## how to run in development mode:
```bash
cd {vehicles-monitor repo dir}/website
pipenv shell
python3 manage.py runserver
```
## This component uses  
* [Django](https://www.djangoproject.com/) web framework
* [Nameko](https://nameko.readthedocs.io/en/stable/) microservices framework
* [RabbitMQ](https://www.rabbitmq.com/) message broker
* [PostgreSQL](https://www.postgresql.org/) relational database
* [Tabulator](http://tabulator.info/) interactive table javascript library

## API
this component has only one endpoint:

**url**: /vehicles/  
**method**: GET  
**description**: This endpoint retrieves all the vehicles stored permanently on PostgreSQL datababase and for each 
vehicles it sets the state retrieved from the monitoring service  

## UI
This component has only one page (/) which is a table of all vehicles beside its state, 
it uses Tabulator as an interactive table which contains filtering and sorting features out of the box.

## Future work
* Authentication 
* Use single page framework (Angular, Vue, React, ...) for the ui in cas we need more advanced ui.
* Add filtering features to vehicles endpoint in case we don't need to retrieve all the data
* use `guincorn` to serve the website over a socket and `nginx` as proxy to this socket