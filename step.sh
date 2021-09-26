#!/bin/bash
if [[ ! -d "Bosch" ]]; then
	echo "Creando entorno virtual..."
	python3 -m venv Bosch
	echo "Clonando repositorio..."
	cd Bosch
	git clone https://github.com/sebabosch/todo-django.git
	cd ..
fi
cd Bosch
source bin/activate
echo "Verificando dependencias"
pip3 install -r req.txt
cd todo-django
"Iniciando servidor..."
python3 manage.py runserver
