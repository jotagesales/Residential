from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'Residential.views.home', name='home'),
                       url(r'sobre', 'Residential.views.sobre', name='sobre'),
                       url(r'cadastro', 'Residential.views.cadastro', name='cadastro'),
                       url(r'contato', 'Residential.views.contato', name='contato'),
                       url(r'portfolio', 'Residential.views.portfolio', name='portfolio'),
                       url(r'servico', 'Residential.views.servicos', name='servico'),
                       url(r'^admin/', include(admin.site.urls)),
)
