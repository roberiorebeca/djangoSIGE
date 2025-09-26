# -*- coding: utf-8 -*-

from django.urls import path, re_path, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('djangosige.apps.base.urls')),
    path(r'login/', include('djangosige.apps.login.urls')),
    path(r'cadastro/', include('djangosige.apps.cadastro.urls')),
    path(r'fiscal/', include('djangosige.apps.fiscal.urls')),
    path(r'vendas/', include('djangosige.apps.vendas.urls')),
    path(r'compras/', include('djangosige.apps.compras.urls')),
    path(r'financeiro/', include('djangosige.apps.financeiro.urls')),
    path(r'estoque/', include('djangosige.apps.estoque.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
