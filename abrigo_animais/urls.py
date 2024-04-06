from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from site_abrigo.views import site, detalheAdotar, detalhes_animal, sucesso

urlpatterns = [
    path("admin/", admin.site.urls),

    #? def views site:
    path("", site),
    # http://127.0.0.1:8000

    path("adocoes/", include("adocoes.urls"), name="adocoes"),

    #? def views base_form_detalhe_adocao:
    path("detalhe_adotar/", detalheAdotar),
    # http://127.0.0.1:8000/detalhe_adotar/

    #? rever
    path('animal/<int:animal_id>/', detalhes_animal, name='detalhes_animal'),
    # http://127.0.0.1:8000/animal/1/

    path('sucesso/', sucesso, name='sucesso'),
    # http://127.0.0.1:8000/sucesso/

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# "+ static" é uma maneira de adicionar URLs de arquivos de mídia aos urlpatterns no Django
