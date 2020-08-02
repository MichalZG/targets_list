#!/bin/bash

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${DATABASE_ADMIN_NAME}', '', '${DATABASE_ADMIN_PASS}')" | python manage.py shell

