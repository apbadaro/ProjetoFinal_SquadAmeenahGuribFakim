# Sistema de Gestão de Adoções
_Responsável: [Ana Paula Badaró](https://github.com/quasiEvil)_

Sistema de gerenciamento de adoções de animais: os usuários podem solicitar a adoção de um animal, e os responsáveis pelo abrigo podem aprovar ou recusar as solicitações.

## Estrutura do repositório
O projeto encontra-se dividido em duas partes:
1. Abrigo de Animais (`abrigo_animais`): Projeto principal.
2. Adoções (`adocoes`): App para gerenciar as adoções.

### 1. Abrigo de Animais (`abrigo_animais`)
Contém as configurações do projeto e a configuração do banco de dados.

**Configurações**
- `settings.py`: Configurações do projeto, incluindo `LOGIN_URL` e `MEDIA_URL`.
- `urls.py`: URLs do projeto, incluindo o prefixo para o aplicativo `adocoes`.

### 2. Adoções (`adocoes`)
Sistema de gerenciamento das adoções.

**Modelos**
- `models.py`: Modelos de dados para as adoções, animais, solicitantes e funcionários.

**Formulários**
- `forms.py`: Formulários para as adoções.

**Views**
- `views.py`: Visualizações para gerenciar adoções, incluindo lista completa, detalhes, criação, atualização e exclusão.

**URLs**
- `urls.py`: URLs do app `adocoes`.

**Templates**
- `templates/adocoes/adocoes.html`: Exibe todas as adoções registradas.
- `templates/adocoes/adocao_form.html`: Formulário para criar e atualizar adoções.
- `templates/adocoes/adocao_detalhes.html`: Detalhes de uma adoção específica.
- `templates/adocoes/adocao_excluir_confirmacao.html`: Página de confirmação de exclusão de uma adoção.

## Funcionalidades
- **Cadastro de usuários:** Os usuários podem se cadastrar no sistema como solicitantes.
- **Solicitação de adoção:** Os solicitantes podem solicitar a adoção de um animal disponível.
- **Gerenciamento de adoções:** Os responsáveis pelo abrigo podem visualizar e gerenciar as solicitações de adoção pendentes.
- **Aprovação/Recusa de adoções:** Os responsáveis pelo abrigo podem aprovar ou recusar as solicitações de adoção.

## Tecnologias Utilizadas
- Django
- Python
- SQLite

## Como utilizar
1. Clone o repositório
``` bash
git clone https://github.com/quasiEvil/projeto-final-womakerscode.git

ou

git clone git@github.com:quasiEvil/projeto-final-womakerscode.git
```

2. Navegue até o diretório do projeto:
``` bash
cd projeto-final-womakerscode
```

3. Instale as dependências necessárias. É recomendável criar um ambiente virtual antes disso:
``` bash
pip install -r requirements.txt
``` 

4. Execute as migrações do banco de dados:
``` bash
python manage.py migrate
```

5. Crie um superusuário para acessar a área de administração:
``` bash
python manage.py createsuperuser
```
Siga as instruções para fornecer um nome de usuário, endereço de e-mail (opcional) e senha. Por exemplo:

- Nome de usuário: admin
- Endereço de e-mail: (deixe em branco)
- Senha: 123

6. Inicie o servidor:
``` bash
python manage.py runserver
```

7. Acesse o seguinte endereço em um navegador:
```
http://127.0.0.1:8000/admin

ou

http://localhost:8000/admin
```

8. Faça o login usando as credencias do superusuário criado na etapa 5. Você terá acesso à área de administração, onde poderá gerenciar os usuários, animais e adoções.

## Documentações e referências:
- [Django: Authentication System](https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views)
- [Django: get_object_or_404](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404)
- [Django: HttpResponseServerError](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse)
- [Django: Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)
- [Django: Customizing the Django Admin](https://earthly.dev/blog/customize-django-admin-site/)
- [Django: The Django Admin Site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
- [Django: Creating an admin user](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)
- [Django: Registration](https://www.pythontutorial.net/django-tutorial/django-registration/)
- [Django: File Uploads](https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/)
- [Django: verbose_name](https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/)
- [Django: on_delete](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete)
- [Django: Retrieving Objects](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-objects)
- [Django: How to Change "app name"](https://stackoverflow.com/questions/26972625/how-to-change-app-name-in-django-admin)
