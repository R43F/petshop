# petshop
Instalar anviente virtual com Python 3 <br>
https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/ <br>
1 > python -m venv myvenv -> Instalar Virtualenv¹ <br>
2 > myvenv\Scripts\activate -> Ativar Ambiente virtual <br>
3 > python -m pip install --upgrade pip   -> Atualizar o pip <br>
4 > pip install Django==2.2 - > Instalar o Django <br>
5 > pip install --upgrade setuptools -> Atualizar setuptools <br><br>
¹ Se não conseguir instalar o virtualenv não tem problema, é so padrão utilizar ambientes virtuais. <br>

Apos clonar o diretorio, entre na pasta raiz e rode os comandos abaixo <br>
python manage.py makemigrations <br>
python manage.py migrate <br>
python manage.py runserver <br>

acesse localhost:8000 no seu browser <br>
