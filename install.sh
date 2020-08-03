source .env
docker-compose run -d db 
docker-compose run dbapp python manage.py migrate
docker-compose run dbapp python manage.py makemigrations targets
docker-compose run dbapp python manage.py migrate targets
docker-compose run -e DATABASE_ADMIN_NAME=$DATABASE_ADMIN_NAME -e DATABASE_ADMIN_PASS=$DATABASE_ADMIN_PASS dbapp sh ./create_superuser.sh
