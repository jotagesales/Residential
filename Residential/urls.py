import django.conf.urls
from django.contrib import admin

urlpatterns = django.conf.urls.patterns('',
                       # Examples:
                       django.conf.urls.url(r'$', 'Residential.views.home', name='home'),

                       django.conf.urls.url(r'contato', 'Residential.views.contato', name='contato'),

                       django.conf.urls.url(r'erro', 'Residential.views.erro', name='erro'),

                       django.conf.urls.url(r'^admin/', django.conf.urls.include(admin.site.urls)),
                                        )
