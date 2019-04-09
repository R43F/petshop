# petshop
Instalar anviente virtual com Python 3 <br>
https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/
1 > python -m venv myvenv -> Instalar Virtualenv¹
2 > myvenv\Scripts\activate -> Ativar Ambiente virtual
3 > python -m pip install --upgrade pip   -> Atualizar o pip
4 > pip install Django==2.2 - > Instalar o Django
5 > pip install --upgrade setuptools -> Atualizar setuptools
6 > pip install mysql-connector-python
--> crir um arquivo requirements.txt com o codigo abaixo
mysqlclient==1.4.2
7 > pip install -r requirements.txt

¹ Se não conseguir instalar o virtualenv não tem problema, é so padrão utilizar ambientes virtuais.




Instalar cliente Mysql no Linux
sudo apt-get install python-dev default-libmysqlclient-dev
pip install mysqlclient


Apos clonar o diretorio, entre na pasta raiz e rode os comandos abaixo
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

acesse localhost:8000 no seu browser
