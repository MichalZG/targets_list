#!/bin/bash

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${TARGETS_DATABASE_ADMIN_NAME}', '', '${TARGETS_DATABASE_ADMIN_PASS}')" | python manage.py shell

