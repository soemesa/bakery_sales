# Projeto para venta de padaria online 
Django 3.1.6 e Python 3.12.0

### Para rodar o projeto

```
git clone git@github.com:soemesa/bakery_sales.git
```
* Criar banco de dado `padaria_db` em servidor mysql
* No arquivo loja/settings.py:86 mudar as configurações do banco como usuário e senha

- Para **Linux**:

```
cd bakery
python -m venv venv
. venv/bin/activate
pip install install -r requirements.txt
python manage.py migrate
```

- Para **Windows**:

```
cd bakery
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install -r requirements.txt
python manage.py migrate
```

### Criar super usuário (necessário para aumentar o estoque)
```
python manage.py createsuperuser
```

### Para acessar ao site 
```
http://localhost:8000
```

### Para aumentar o estoque dos produtos da padaria
```
http://localhost:8000/admin
```
* Utilizar o super user criado

