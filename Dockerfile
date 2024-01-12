FROM python:3.8

#pasa el directorio de trabajo a DENTRO DEL CONTENEDOR
WORKDIR /app 

#copia desde el host y lo pega en el contenedor para que pueda usarlo luego en los comandos siguientes de instalacion
COPY requirements.txt requirements.txt
#Lo corre en el contenendor
RUN pip3 install -r requirements.txt --upgrade
COPY . .
#CMD se usa para definir el comando por defecto al empezar el container
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
