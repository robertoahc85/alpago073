#!/usr/bin/env bash
# Salir en caso de error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos sin interacción
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate
