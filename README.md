# Projeto para venta de padaria online 
Django 4.2.7 e Python 3.12.0

### Para rodar o projeto

```
git clone git@github.com:soemesa/bakery_sales.git
```
* Criar banco de dado `padaria_db` em servidor mysql
* No arquivo loja/settings.py:91 mudar as configurações do banco como usuário e senha

- Para **Linux**:

```
cd bakery_sales
python -m venv venv
. venv/bin/activate
pip install install -r requirements.txt
python manage.py migrate
```

- Para **Windows** (Não testado por não ter Sitema Operacional):

```
cd bakery_sales
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

## Pupular banco de dados para preencher registros para teste
```
python manage.py dbrestore
```
### No backup muda o super user
```
user: admin
password: wasaloko
```

# Prints do site
### Tela inicio
![inicio.png](utils/readme/inicio.png)

### Tela de login e cadastro
![login_cadastro.png](utils/readme/login_cadastro.png)

### Tela de lista de produtos
![lista_produtos.png](utils/readme/lista_produtos.png)

### Barra de navegação de tipos de proutos
![nav_produtos.png](utils/readme/nav_produtos.png)

### Filtro de produtos
![filtrando_produtos.png](utils/readme/filtrando_produtos.png)

### Busca produtos
![busca_produtos.png](utils/readme/busca_produtos.png)

### Detalhe produto
![detalhe_produto.png](utils/readme/detalhe_produto.png)

### Adicionado ao carrinho
![adicionado_carrinho.png](utils/readme/adicionado_carrinho.png)

### Lista no carrinho
![carrinho.png](utils/readme/carrinho.png)

### Resumo da compra
![resumo_compra.png](utils/readme/resumo_compra.png)

### Pedido Realizado
![pedido_realizado.png](utils/readme/pedido_realizado.png)

### Pagamento feito
![pagamento_feito.png](utils/readme/pagamento_feito.png)



