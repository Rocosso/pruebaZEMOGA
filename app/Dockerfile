FROM python:3.11.0b1-alpine3.15
# importamos imagen del SO, con Python previamente preinstalado y
# con ambas versiones especificadas para evitar que actualizaciones futuras saquen de linea la app
RUN adduser -D -g '' appoperator
USER appoperator


# adduser [OPTIONS] user_name
# Add a user
# Options:
#        -h DIR          Home directory
#        -g GECOS        GECOS field
#        -s SHELL        Login shell
#        -G GRP          Add user to existing group
#        -S              Create a system user
#        -D              Do not assign a password
#        -H              Do not create home directory
#        -u UID          User id


# creamos un grupo y un usuario, seleccionamos un usuario, de preferencia un suoder <-S>,
# no SUDO ni root (por estabilidad y seguridad).

WORKDIR /usr/src/bin
# creamos el directorio del contexto

# copiamos todo el contexto dentro de la imagen de Docker
COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt
    # damos permisos e instalamos requerimientos de python3 usando PIP

EXPOSE 8080/tcp
# activamos el puerto 8080 dentro del contenedor para ejecutar la app

CMD [ "python3", "app.py" ]
# invocamos la ruta de la app para ejecutar


