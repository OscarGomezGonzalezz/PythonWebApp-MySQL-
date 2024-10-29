El proyecto consiste en una página web implementada con Flask, un framework de Python. Esta a su vez, esta conectada a una base de datos MySQL,
a la cual podremos acceder como veremos posteriormente. Todo esto, siendo implementado con docker-compose, facilitando así el despliegue y la gestión,
tanto de contenedores como de las redes a las que pertenecen estos mismos, a la cual en nuestro caso hemos integrado ambos conectores para su mutua interacción .

En primer lugar iniciamos el server de python desde docker desktop o desde la terminal

Para ejecutar el servidor de mysql, necesitaremos tener en un mismo directorio todos los archivos presentes en el repositorio. Una vez los tengamos implementados(están todos explicados
mediante anotaciones), ejecutaremos:

docker-compose -f ./docker-compose.dev.yml up -d --build 

De este modo, habremos construido e iniciado en segundo plano todos los contenedores pertenecientes al docker-compose.
Para comprobarlo, podremos hacer:

docker ps

Si la columna 'State' indica 'up' podremos proseguir, en caso contrario, es recomendable ver errores con 'docker logs nombre_contenedor'
A continuación, para comprobar el correcto funcionamiento de la app, iniciaremos la base de datos con:

curl localhost:5001/initdb 

Iniciaremos la tabla:

curl localhost:5001/init_tables

Y, para finalizar, comprobaremos la conectividad con la tabla ejecutando:

curl localhost:5001/universities

De este modo, la App ejecutará la operacion "SELECT * FROM Universities",y transformará lo devuelto mediante una representación JSON a una respuesta http,
pero en nuestro caso, al no haber hecho aún los inserts, nos devolverá una lista vacía.

Para ello, 

curl localhost:5001/insert

Y finalmente,volviendo a ejecutar la ruta /universities veremos que ,en efecto, nos devolverá una lista con la información sobre el MIT y la Boston College.

