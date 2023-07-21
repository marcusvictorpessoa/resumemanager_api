
# API do ResumeManager

## Como rodar o projeto

* Versão do python para rodar o projeto: 3.11.4

* Para linux, substituir comando python por python3, se o python2 estiver instalado

1. Após clonar o projeto entre na pasta e crie o ambiente virtual:

    > cd resumemanager_api
    > python -m venv .

* Verificar se o arquivo "pyvenv.cfg" no campo "version" é igual a versão 3.11.4

2. Após ativar o Virtual Env, baixe as dependências do projeto:

    > pip install -r requirements.txt

3. Rode os comandos para executar as migrações:

    > python manage.py makemigrations
    > python manage.py migrate

4. Crie o usuário Admin:

    > python manage.py createsuperuser

5. Rode o projeto:

    > python manage.py runserver

* Acessar o [Sistema Admin](http://localhost:8000/admin/)

### Rotas

* [API Base URL](http://localhost:8000/api/v1)

| Rota                 | Método | Descrição                    |
|----------------------|--------|------------------------------|
| /auth/jwt/create/    | POST   | Gera o token de autenticação |
| /auth/jwt/refresh/   | POST   | Gera o novo token            |
| /auth/jwt/verify/    | POST   | Verifica se o token é válido |
| /candidates/         | GET    | Lista candidatos             |
| /candidates/         | POST   | Cria candidatos              |
| /candidates/{uuid}/  | GET    | Mostra candidato             |
| /candidates/{uuid}/  | PUT    | Atualiza campos do candidato |
| /candidates/{uuid}/  | PATCH  | Atualiza campos do candidato |
| /candidates/{uuid}/  | DELETE | Deleta candidato             |