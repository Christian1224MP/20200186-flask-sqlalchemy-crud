##Ejemplo de API Rest CRUD con flask
## App que implementa rutas en Python con framework Flask,Jinja y Bd Postgresql

# Descargar el proyecto desde github:
1.Descargar el proyecto desde github
2.cree el archivo .env localmente con los parametros de conexion a la base de datos 
o descarguelo del classroom del curso

POSTGRESQL_USER = TUUSUARIO
POSTGRESQL_PASSWORD = TUPWD
POSTGRESQL_DATABASE = NOMBREBD
POSTGRESQL_HOST = IPSERVER
POSTGRESQL_SERVER = postgresql

# Levantar el proyecto en ambiente local
Para ingresar al entorno virtual:
desde la ruta del proyecto lanzar el siguiente comando:

virtualenv venv

#para activar el entorno virtual, desde la ruta del proyecto lanzar el siguiente comando:
venv\Scripts\activate

#una vez activado el entorno virtual debe mostrar como se indica:
(venv) PS C:\RutaDelProyecto

#luego lanzar la instruccion para instalar las dependencias:
pip install -r requirements.txt

#para activar el modo debug con flask:
#añadir una variable de entorno FLASK_DEBUG=1

#para desplegar en ambiente local:
flask run

#Comandos ejecutados necesarios para el funcionamiento del proyecto desde cero
  Id CommandLine                                                                                                                                                         
  -- -----------                                                                                                                                                         
   0 virtualenv venv
   1 venv\Scripts\activate                                                                                                                                               
   2 pip install flask                                                                                                                                                      
   3 pip show Flask-Cors                                                                                                                                                          
   4 pip install Flask-SQLAlchemy                                                                                                                                        
   5 pip install psycopg2                                                                                                                                                
   6 pip install dataclasses                                                                                                                                                 
   7 pip install python-dotenv                                                                                                                                           
   8 pip freeze >requirements.txt                                                                                                                                        
   9 python app.py                                                                                                                                                       
  10 flask run                                                                                                                                                                                                                                                                                                                       
  11 flask run --port 5000                                                                                                                                               

#Comando para obtener las dependencias de la app
pip freeze >requirements.txt

#Comando para obtener el historico de comandos ejecutados en la consola de vscode
Get-History | Out-File myhistory.txt

#Otros comandos de interes
python -m pip install wheel
python.exe -m pip install --upgrade pip
python -m pip install virtualenv

# Para instalar el paquete pip si no se encuentra en la carpeta de instalacion de python:
python -m pip install -U pip