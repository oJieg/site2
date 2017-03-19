"""
Definition of urls for DjangoWebProject3.
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^one/', include('one.urls')),
    url(r'^admin/', admin.site.urls),
]

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

