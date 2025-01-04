!/usr/bin/env bash
# build.sh

echo "Building the project..."
set -o errexit

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Crear directorio static si no existe
mkdir -p static

# Limpiar staticfiles
rm -rf staticfiles/*

# Asegurarse de que el directorio staticfiles existe
mkdir -p staticfiles

# Copiar archivos admin manualmente (por si acaso)
python manage.py collectstatic --noinput


# Verificar la recolección de estáticos
echo "Verificando archivos estáticos..."
ls -la staticfiles/admin/css/

# Establecer permisos
echo "Estableciendo permisos..."
chmod -R 755 staticfiles/

# Realizar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# # Crear superusuario si es necesario (opcional)
# if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#     python manage.py createsuperuser \
#         --noinput \
#         --username $DJANGO_SUPERUSER_USERNAME \
#         --email $DJANGO_SUPERUSER_EMAIL
# fi