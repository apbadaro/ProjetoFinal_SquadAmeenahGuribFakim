from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from site_abrigo.views import site, animais_disponiveis
from detalhe_pedido.views import detalhe_pedido, sucesso, doar, cuidador, voluntario, sobre, agenda
from detalhe_pedido import views

urlpatterns = [
    path("admin/", admin.site.urls),

    #? def views site:
    path("", site),
    # http://127.0.0.1:8000

    path("adocoes/", include("adocoes.urls"), name="adocoes"),

    path('animais_disponiveis/', animais_disponiveis),

    path('detalhe_pedido/<int:animal_id>/', views.detalhe_pedido, name='detalhe_pedido'),
    # http://127.0.0.1:8000/detalhe_pedido/

    path('sucesso/', sucesso, name='sucesso'),
    # http://127.0.0.1:8000/sucesso/

    # Páginas em Construção:
    path('doar/', doar),

    path('cuidador/', cuidador),

    path('voluntario/', voluntario),

    path('sobre/', sobre),

    path('agenda/', agenda),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# "+ static" é uma maneira de adicionar URLs de arquivos de mídia aos urlpatterns no Django
