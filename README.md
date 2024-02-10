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

- Flask
- python-barcode
- pillow