# Establecer la imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el Pipfile y Pipfile.lock al directorio de trabajo
COPY Pipfile Pipfile.lock ./

# Instalar las dependencias utilizando el archivo Pipfile.lock
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copiar el resto de los archivos de la aplicación
COPY . .

# Especificar el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["pipenv", "run", "python", "app.py"]
