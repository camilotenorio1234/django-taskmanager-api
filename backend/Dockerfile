# Imagen base
FROM python:3.11

# Crear directorio de trabajo
WORKDIR /code

# Copiar archivos
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /code/

# Puerto expuesto
EXPOSE 8000

# Comando para correr Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
