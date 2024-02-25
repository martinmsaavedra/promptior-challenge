# Establecer la imagen base
FROM python:3.9-slim

# Instalar una versión específica de pipenv
RUN pip install pipenv==2023.12.1

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el Pipfile y Pipfile.lock al directorio de trabajo
COPY Pipfile Pipfile.lock ./

# Instalar las dependencias utilizando el archivo Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Copiar el resto de los archivos de la aplicación
COPY . .

# Especificar el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["pipenv", "run", "python", "app.py"]
