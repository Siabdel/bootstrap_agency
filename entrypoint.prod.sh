#! /bin/sh
if [ " $ DATABASE " = "postgres" ]
    then
        echo "En attente de postgres ..."
        while ! nc -z $ SQL_HOST $ SQL_PORT ; do
            sleep 0 .1
        done
    echo
    "PostgreSQL a démarré"
fi

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
#
pip install python-dotenv
#python3 manage.py flush --no-input
#python3 manage.py migrate --noinput;
rm -r staticfiles/*
# Collect static files.
python3 manage.py collectstatic --noinput --clear
## creation du superuser abdel et admin
#echo "from django.contrib.auth.models import User; User.objects.create_superuser(username='admin', password='grutil001', email='admin@atlass.fr')" | python3 manage.py shell
#echo "from django.contrib.auth.models import User; User.objects.create_superuser(username='abdel', password='grutil001', email='abdel@atlass.fr')" | python3 manage.py shell


exec
"$@"