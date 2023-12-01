# AQUA: Aplicativo de monitoramento para sistemas de aquaponia

O presente trabalho tem como objetivo implementar um dashboard que apresentara as métricas de
funcionamento de um sistema de aquaponia. O monitoramento se dá com a
utilização de sensores que se comunicam com um controlador Arduino que transmite os
dados para um aplicativo Django na nuvem, usando um broker MQTT como intermediário.

_Tela do Aplicativo Django_

![Alt Text](https://github.com/barrancocarlos/Aqua-IoT/blob/main/Django/static/assets/img/illustrations/home-aqua.png)

_Sistema IoT_

![Alt Text](https://github.com/barrancocarlos/Aqua-IoT/blob/main/Django/static/assets/img/illustrations/circuits.jpg)

## Guia de instalação rápida

Estas instruções fornecerão uma cópia do projeto em funcionamento em sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

Certifique-se de ter instalado todos os seguintes pré-requisitos em sua máquina de desenvolvimento:

* Git - [Download & Install. Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python - [Download & Install Python](https://www.python.org/downloads/) and the pip package manager.

### Instalação

```bash
# Clonar este repositório
$ git clone https://github.com/barrancocarlos/Aqua-IoT.git

# Entre na pasta
$ cd Django

# Instale dependências no ambiente virtual
$ pip install pipenv
$ pipenv shell
$ pipenv install

# Execute o aplicativo
$ python manage.py runserver