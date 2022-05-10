FROM python:3.11.0b1-alpine3.15            # importamos imagen del SO, con Python previamente preinstalado y
                                           #  con ambas versiones para evitar que cambios futuros arruinen la app

USER root                                  # seleccionamos un usuario, de preferencia un suoder, no SUDO ni root.

WORKDIR /app                               # creamos el directorio del contexto
COPY . .                                   # copiamos todo el contecto dentro de la imagen de Docker
RUN python3 -m venv virtual-env \          # creamos el entorno virtual
    && source virtual-env/bin/activate \   # activamos el entorno virtual creado
    && pip3 install -r requirements.txt    # instalamos requerimientos de python3 usando PIP3

EXPOSE 8080/tcp                            # activamos el puerto 8080 dentro del contenedor para ejecutar la app

CMD ["src/app.py"]                         # invocamos la ruta de la app para ejecutar
ENTRYPOINT ["python3"]                     # indicamos el comando para ejecutarla
