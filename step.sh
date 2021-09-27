#!/bin/bash
if [ ! -f manage.py ]; then
	#Not in todo-django
	if [ ! -d Bosch ]; then
		echo "Creando entorno virtual..."
		python3 -m venv Bosch
		echo "Clonando repositorio..."
		cd Bosch
		git clone https://github.com/sebabosch/todo-django.git
		echo "Activando entorno virtual"
		source bin/activate
		cd todo-django
		echo "Verificando dependencias"
		cd todo-django
		pip3 install -r req.txt
		python3 manage.py migrate
	else
		cd Bosch/todo-django
	fi
else
	echo "Activando entorno virtual"
	source ../bin/activate
fi
echo "Iniciando servidor..."
python3 manage.py runserver
deactivate
