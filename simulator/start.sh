while ! nc -z rabbitmq 5672; do
  sleep 0.1
done

cd /code/
nameko run simulator --broker amqp://guest:guest@rabbitmq:5672