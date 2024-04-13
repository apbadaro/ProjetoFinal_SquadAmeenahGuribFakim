# Sistema de Gestão de Adoções
_Responsável: [Ana Paula Badaró](https://github.com/quasiEvil)_

Sistema de gerenciamento de adoções de animais: os responsáveis pelo abrigo podem aprovar ou recusar as solicitações de adoção.

## Aplicativo de adoções (`adocoes`)
Sistema de gerenciamento das adoções do abrigo.

**Modelos**
- `models.py`: Modelos de dados para as adoções, animais, solicitantes e funcionários.

**Formulário**
- `form.py`: Formulário para as adoções.

**Views**
- `views.py`: Visualizações para gerenciar adoções, incluindo a listagem completa, detalhes, criação, atualização e exclusão.

**URLs**
- `urls.py`: URLs do app `adocoes`.

## Funcionalidades
- **Cadastro de solicitantes, animais e funcionários:** Registra novos dados de solicitantes, animais e funcionários na área do administrador com permissão de superusuário.

- **Gerenciamento de adoções:** Administração e visualização das solicitações de adoção.

- **Aprovação/Recusa de adoções:** Possibilidade de aceitar ou recusar as solicitações de adoção.

## Acessando a área do `admin`
1. Acesse o seguinte endereço em um navegador:
``` bash
https://squadameenahguribfakim.pythonanywhere.com/admin
```

2. Faça o login com alguma das credenciais abaixo:
``` bash
Clarice, Gerente (permissão de superuser)
Usuário: clarice
Senha: senha123
```

``` bash
Danilo, Voluntário (permissão restrita de voluntário)
Usuário: danilo
Senha: senha123
```

## Tecnologias utilizadas
- Bootstrap 5
- Django
- Pillow
- Python
- SQLite

## Documentações e referências:
- [Django: Authentication System](https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views)
- [Django: get_object_or_404](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404)
- [Django: HttpResponseServerError](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse)
- [Django: Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)
- [Django: Customizing the Django Admin](https://earthly.dev/blog/customize-django-admin-site/)
- [Django: The Django Admin Site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
- [Django: Creating an admin user](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)
- [Django: Registration](https://www.pythontutorial.net/django-tutorial/django-registration/)
- [Django: File and Image Uploads](https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial)
- [Django: verbose_name](https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/)
- [Django: on_delete](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete)
- [Django: Retrieving Objects](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-objects)
- [Django: How to Change "app name"](https://stackoverflow.com/questions/26972625/how-to-change-app-name-in-django-admin)
- [Django: CSRF Protection](https://docs.djangoproject.com/en/5.0/ref/csrf/)
