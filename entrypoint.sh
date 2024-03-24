#!/bin/sh -

set -o errexit
set -o nounset

cd stripes_with_pride/

case $1 in
    dev)
        nohup python manage.py migrate --settings=stripes_with_pride.settings.local --noinput &
        nohup python manage.py collectstatic --settings=stripes_with_pride.settings.local --clear --noinput &
        exec python manage.py runserver 0.0.0.0:8000 --settings=stripes_with_pride.settings.local;;
    migrate)
        exec python manage.py migrate --settings=stripes_with_pride.settings.local --noinput;;
    *)
        echo "error: $1 is not a valid entrypoint script argument.  Exiting..."
        exit 1;;
esac
