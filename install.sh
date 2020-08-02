docker-compose run dbapp python manage.py migrate
docker-compose run dbapp python manage.py makemigrations targets
docker-compose run dbapp python manage.py migrate targets
docker-compose run dbapp sh ./create_superuser.sh
