# Projeto NLW Python

Este é um projeto inspirado no nlw de fevereiro da rocketseat para utilização de python para criação de uma aplicação baseada em códigos de barra.

## Configurando o ambiente

O primeiro passo é criar um ambiente virtual para a instalação de pacotes e configuração de ambiente utilizando venv.
Para isso 3 coisas são necessárias:
1. Python3 instalado
2. python3-pip instalado
3. python3-venv instalado

Para executar o ambiente usando `.venv` você pode simplesmente rodar o seguint comando:

```shell
. .venv/bin/activate
```
>onde o primeiro ponto é apenas para direcionar para o diretório atual.

Após isso feito, podemos instalar os pacotes `pylint` e `pre-commit`, através dos comandos

```shell
pip3 install pylint
pip3 install pre-commit
```

Agora podemos criar os arquivos de configuração `.pylintrc` e `.pre-commit-config.yml` para configurar um hook de pre-commit e setar as configurações de lint do projeto, onde rodar o comando:

```shell
pylint --generate-rcfile > .pylintrc
```
> Esse comando gera o arquivo .pylintrc automatically

### Bibliotecas necessárias

Antes de exibir as bibliotecas necessárias, primeiro é recomendado que você tenha o arquivo `requirements.txt` no seu projeto para que seja possível identificar as bibliotecas necessárias para o funcionamento do seu projeto.
Para isso basta executar o comando:

```shell
.venv/bin/pip3 freeze > requirements.txt
```

Agora podemos fazer a instalação dos pacotes principais que são eles:

- Flask - Um framework web para construção de apis robustas e escaláveis
- python-barcode - Uma biblioteca feita para criação de imagens de código de barra à partir de strings
- pillow - Uma dependência necessária para o funcionamento da biblioteca python-barcode
- cerberus - Uma biblioteca utilizada para validação robusta e prática
- pytest - Biblioteca utilizada para criação de testes unitários em python

## Architecture (EN)

Ok, you have just installed things, and now you will structure your code to create a modular application with the right responsibilities.

First, your code has to use the pattern of routes and server with blueprints of Flask, which allows you to register your routes with a few lines of code.

>[!IMPORTANT]
> You have to create a `__init__.py` file on each module to allow you to import them from other sources in your codebase.

### Source tree
Your source code will be like this:

```bash
.
├──📝 requirements.txt
├──🐍 run.py
└──📂 src
   ├──🐍 __init__.py
   ├──📂 main
   │   ├──🐍 __init__.py
   │   │
   │   ├──📂 routes
   │   │   ├──🐍 __init__.py
   │   │   │
   │   │   └──🐍 your_route.py
   │   └──📂 server
   │       ├──🐍 __init__.py
   │       │
   │       └──🐍 server.py
   │
   ├──📂 views
   │    ├──📂 http_types
   │    │   ├──🐍 http_request.py
   │    │   ├──🐍 http_response.py
   │    │   └──🐍 __init__.py
   │    │   
   │    ├──🐍 __init__.py
   │    │
   │    └──🐍 your_route_view.py
   ├──📂 drivers
   │    ├──🐍 __init__.py
   │    │ 
   │    └──🐍 your_lib_driver.py
   ├──📂 errors
   │    ├──📂 error_types
   │    │   ├──🐍 http_unprocessable_entity.py
   │    │   ├──🐍 http_unauthorized_entity.py
   │    │   └──🐍 __init__.py
   │    ├──🐍 error_handler.py
   │    └──🐍 __init__.py
   ├──📂 validators
   │    ├──🐍 __init__.py
   │    │ 
   │    └──🐍 your_route_validator.py   
   │
   └──📂 controllers
        ├──🐍 __init__.py
        │ 
        └──🐍 your_business_controller.py         

```

Each directory has a significant job

directory|description
:---:|:---:
main|This is where your application is created, classes will be instanced and all logic of routes is used
routes|This is where you can make your blueprint routes to encapsulate the logic of each different route
server|This is where you can register all of your created blueprints in your application to be used on the server
views|This is where you can make your types and classes to make sure that your app will work as expected
drivers|This is where you have to encapsulate your libraries to ensure that if something goes wrong you can easily migrate to another solution
controllers|This is where you must apply the business logic that is just responsible for that.
errors|This is where your application handles errors, customized or not.
error_types|This is where your application creates customized errors
validators|This is where you can create different validations on your application

> The run.py is used to run your application in a specific host and port


### Creating a blueprint

In the `routes` directory, you will create a file with a suggestive name to your purpose, like `user_routes.py`.
```python
from flask import Blueprint, jsonify, request

user_routes_bp = Blueprint("user_routes", __name__)

#...rest of your code

```

>[!NOTE]
> This will just create an instance of Blueprint of Flask with a signature "user_routes"

then you can create any route with any method related to that blueprint

```py
#... example above

@user_routes_bp.route("/create_user",methods=["POST"])
def create_user():
  ### business logic here

@user_routes_bp.route("/user",methods=["GET"])
def get_user():
  ### business logic here

@user_routes_bp.route("/user/:id",methods=["DELETE"])
def delete_user():
  ### business logic here
```

### Registering blueprint

This is quite simple to do, you just need to import your blueprint in the `server` directory from the `routes` directory then use `app.register_blueprint(imported_blueprint)`, and done!

### Creating a Customized Error

This is the finesse of inheritance and polymorphism, here in our codebase we actually can create any error type for our project.
This is because Python is an object-oriented language, that allows us to work very well with that concept.

So to create a http_unauthorized_entity error, you can follow these steps:

1. create a module responsible for containing the class `HttpUnauthorizedEntity`
2. Then you use the concept of polymorphism like this:
  ```python
  class HttpUnauthorizedEntity(Exception): # this receive an Exception as argument
    def __init__(self, message:str): # this is the constructor
      self.message = message
      self.status_code = 401
      self.name = "Unauthorized Entity"
      super().__init__(self.message) # This call the constructor of the inherited class and passes the message to the argument

  ```

> And that's it! This is a Customized error class that inherits from the Exception interface

To verify if a object `obj` is an instance of `customized_class` you can use the `isInstance(obj,customized_class)` that returns a `Boolean`.

>[!NOTE]
> The reserved word for throw an error in python is raise
## Tests

So, now, we can talk about tests!

The approach that we use here is creating the test in the same directory that the module that will be tested. This will help us to import easily the tested module.

### The test name

Easier impossible, you can just put a `_test` before `.py` and that's it! Pytest identifies the file.

### Arrange, act, assert
Those 3 things is the philosophy for unit tests in pytest, and is a good way to start writing tests.

#### Arrange
To `arrange` your modules, the smartest way is mocking your case tests. In case that you find yourself testing some feature that you don't care about you can use the `patch` decorator from `unittest.mock` that allow you to mock some result from a class. The syntax is simple:

```py

from unittest.mock import patch
from foo.bar.module import NotCareAboutThisFunctionality
from .tested_module import AwesomeFunctionality

# This can be anything, here we using as NotCareAboutThisFunctionality instance mocking the mocked_method
@patch.object(NotCareAboutThisFunctionality, "awesome_method")
def test_your_module(mocked_awesome_method):
    # This will take care that the returned method from the awesome_method
    # will be a wanted value 
    mocked_awesome_method.return_value = 'mocked_value'
    mocked_instance = AwesomeFunctionality()
    # This method call NotCareAboutThisFunctionality.awesome_method in somewhere
    result = mocked_instance.awesome_feature()
    # ... assert things only about AwesomeFunctionality
```
#### Act
Act is just what you need to do to test your case
In the above code, the `mocked_instance.awesome_feature()` is an example of act in unit tests

#### Assert

Just verify if the result is what you expect, with python, the reserved word is also `assert`:

> ### Full example:
>  ```py
>
>  from unittest.mock import patch
>  from foo.bar.module import NotCareAboutThisFunctionality
>  from .tested_module import AwesomeFunctionality
>
>  # This can be anything, here we using as NotCareAboutThisFunctionality instance mocking the mocked_method
>  @patch.object(NotCareAboutThisFunctionality, "awesome_method")
>  def test_your_module(mocked_awesome_method):
>      
>      # arrange
>
>      # This will take care that the returned method from the awesome_method
>      # will be a wanted value 
>      mocked_awesome_method.return_value = 'mocked_value'
>      mocked_instance = AwesomeFunctionality()
>      
>      # act
>
>      # This method call NotCareAboutThisFunctionality.awesome_method in somewhere
>      result = mocked_instance.awesome_feature()
>
>      # assert
>      
>      assert result == 'expected_value'
>      assert result != 'unexpected_value'
>  ```