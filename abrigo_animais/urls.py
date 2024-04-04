from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from site_abrigo.views import site

urlpatterns = [
    path("admin/", admin.site.urls),
    #? def views site:
    path("site/", site),
    # http://127.0.0.1:8000/site
    path("adocoes/", include("adocoes.urls"), name="adocoes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# "+ static" é uma maneira de adicionar URLs de arquivos de mídia aos urlpatterns no Django
