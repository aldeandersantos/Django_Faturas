# Django Faturas

Django Faturas é um projeto desenvolvido em Django para gerenciar e visualizar faturas.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

- Python (versão 3.9)
- Pipenv (opcional, mas recomendado para controle de ambiente virtual)
  
## Configuração do Ambiente de Desenvolvimento

1. Clone este repositório:

    ```bash
    git clone https://github.com/aldeandersantos/Django_Faturas.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd Django_Faturas
    ```

3. Instale as dependências usando Pipenv:

    ```bash
    pipenv install
    ```

4. Ative o ambiente virtual:

    ```bash
    pipenv shell
    ```

5. Execute as migrações do Django:

    ```bash
    python manage.py migrate
    ```

## Executando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver