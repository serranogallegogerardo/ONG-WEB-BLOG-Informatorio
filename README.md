# Blog Oportunidad de Cambio Grupo 9
[NO OLVIDARSE DE: create DATABASE ongdb]
-ong/settings poner la contraseña que tienen de su mysql
-[estar atentos a la version de mysql...]
-(si da error, fijarse en el apartado de bugs en discord)

probando

Requisitos:
	Python
	PATH
	PIP

python -m venv .vomg

Windows:

	source .vomg/Scripts/Activate

Linux/unix

	source .vomg/bin/activate

pip install -r requirements.txt

Abrir MYSQL workbench -> create database ongdb;
python manage.py runserver

Crear la base de datos 'ongdb' en mysqlworkbench
cambiar la contraseña en ong.settings

python manage.py makemigrations
python manage.py migrate


Se soluciono lo de la estructura

cuenta django
user: grupo9
password: grupo9grupo9

python -m venv .vomg
source .vomg/Scripts/Activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
