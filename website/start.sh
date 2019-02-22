python /code/website/manage.py migrate
python /code/website/manage.py loaddata /code/website/fixtures/initial_data.json
python /code/website/manage.py runserver 0.0.0.0:8000