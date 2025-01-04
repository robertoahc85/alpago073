#!/usr/bin/env bash
# build.sh

# Salir en caso de error
set -o errexit

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del sistema para psycopg2
apt-get update && apt-get install -y \
    postgresql \
    postgresql-contrib \
    python3-dev \
    libpq-dev

# Instalar dependencias de Python
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Realizar migraciones
python manage.py migrate

# Crear superusuario si es necesario (opcional)
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi