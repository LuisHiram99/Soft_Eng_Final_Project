# Sistema-de-Captura
Este proyecto es una aplicación web desarrollada en Django que permite a los usuarios registrarse e iniciar sesión para acceder a visualizaciones gráficas de datos sobre accidentes de tránsito ocurridos en Hermosillo entre los años 2015 y 2021. La aplicación utiliza una base de datos MySQL para almacenar la información de los accidentes y presenta los datos mediante gráficos.
![image](https://github.com/LuisHiram99/Soft_Eng_Final_Project/assets/122404524/204b7292-cf3d-4245-8285-4c96a41f3797)

## Objetivo del proyecto:
El objetivo principal del proyecto es utilizar herramientas de desarrollo web y bases de datos para generar un sistema capaz de registrar, almacenar usuarios y mostrar tablas dinamicas con informacion extraida de otra base de datos. En la foto adjunta podemos ver la interface de singin y singup.
![image](https://github.com/LuisHiram99/Soft_Eng_Final_Project/assets/122404524/c2bad4bf-a89b-4b2c-9211-ac960caca986)
![image](https://github.com/LuisHiram99/Soft_Eng_Final_Project/assets/122404524/72887c29-5cd0-407e-b36c-1334b4bebae2)

## Características del sistema:
- Crear un sistema de inicio/salida de sesión (login/logout).
- Crear múltiples herramientas para que un Administrador pueda modificar/consultar la base de datos que corresponde a los usuarios creados.
- Crear múltiples herramientas para que tanto usuarios como administradores puedan consultar/modificar la base de datos.
## Herramientas tecnológicas que se utilizarán en el proyecto:
- Se hará uso de Django como framework de trabajo, debido a su gran versatilidad y gran apoyo de librerias para desarrollo web.
- Para la parte visual se utilizará HTML y CSS.
- Se utilizó JavaScript para utilidades dinámicas en la página. 
- Como base de datos, se utilizará MySQL.

# Pasos para correr la página web en su propia computadora
1. Instalar Python y MySql en su computadora.
2. Dentro de Python, asegurarse de tener instalada la librería pymysql y django, si no cuenta con ellas, deberá instalarlas. En windows se puede usar el comando pip install PyMySQL para instalar pymysql. Y puede usar pip install django para instalar Django.
3. Haciendo uso de MySql, crear una base de datos llamada usuarios, asignarle un usuario y una contraseña.
4. Descargar el repositorio.
5. Dentro de la carpeta del proyecto "BancoAlimentos", ubicar el archivo settings.py, este archivo contiene multiples configuraciones correspondientes al proyecto, de momento solo deberá modificar la configuración de la base de datos. Para esto vaya a la linea del codigo número 77, la cual dice "DATABASES".
6. Ingresar los datos correspondientes para realizar la conexión con su base de datos MySql. Si desea vincular otra base de datos distinta a MySql, deberá leer la documentación de django.
7. Finalmente, usando la terminar, ubicarse en el directorio del proyecto donde se encuentra el archivo manage.py y ejecucar el comando python manage.py runserver. Si el comando no funciona, use el siguiente comando: py manage.py runserver.
8. Si python arroja un error, debe ser debido a que falta hacer las migraciones de la base de datos, para ello usaremos los siguientes comandos seguidos uno del otro:
   1. python manage.py makemigrations
   2. python manage.py migrate
9. Ejecutamos nuevamente el comando python manage.py runserver.
   
