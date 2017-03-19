from django.conf.urls import url

from . import views

app_name = 'one'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
     url(r'^addcom/$', views.addcom)
    ]