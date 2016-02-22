from django.conf.urls import url

from . import views #para importar las vistas desde el views.py
#Cuando alguien solicita una pagina
#django solicita la url de la pagina y muestra la vista
#Las vistas estan declaradas en el views.py ys son llamadas aqui
#Aqui se definio el nombre de la app 'polls'
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]