# RiskMapDevelop


## Descripción
- El proyecto RiskMap es un proyecto que fue realizado por Jorge Díaz e Isidora Ubilla durante el segundo semestre del 2020.

- Este proyecto buscaba permitir visualizar un mapa de la región de valapariso, marcando las unidades vecinales con un color que dependia del riesgo que habia de contagio en dicha unidad. Además, el mapa debia mostrar los puntos de aglomeración de la región que nombramos varias veces en este proyecto como markets.

- Las carpetas de este proyecto son:

>  * dashboard: En esta carpeta esta el código respecto a las vistas del proyecto cuando el usuario no esta logueado.
>  * login: En esta carpeta esta el código respecto al sistema de iniciar sesión.
>  * media: En esta carpeta se encuentran todas las imagenes utilizadas en el proyecto, y las imagenes que venian con el template.
>  * nginx: En esta carpeta esta la configuración para el docker de nginx que fue necesario para correrlo en el servidor.  Cabe destacar que para este proyecto se utilizó el dominio lc-ip81.inf.utfsm.cl, cambiar por el nombre del dominio donde se haga el deploy del proyecto.
>  * RiskmapApp: Esta carpeta contiene el código original del profesor al comenzar la idea del proyecto. No se ocupa pero se conserva por futuros usos.
>  * RiskmapProject: Esta carpeta contiene la configuración general del proyecto.
>  * staticfiles: En esta carpeta están todos los staticos utilizados para el proyecto.
>  * templates: En esta carpeta están todos los archivos html del proyecto.
>  * userprofiles: En esta carpeta está el código de las vistas de usuario ya logueado.
>  * El resto de los archivos son la configuración del docker.

## Correr el proyecto en Local

- Para la ejecución del proyecto en su local, basta tener un entorno virtual con django instalado y correr el comando:

  > python3 manage.py runserver

  o
  > py manage.py runserver

  dependiendo de su sistema.

## Correr el proyecto en el servidor

-Para correr el proyecto en el servidor nosotros ocupamos los comandos de docker-compose:
>- docker-compose build (para construir el docker)
- docker-compose up -d (para correr el docker)
- docker-compose down -v (para detener el docker)
