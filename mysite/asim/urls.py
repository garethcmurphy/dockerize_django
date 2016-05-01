
from django.conf.urls import url
from django.conf.urls.static import static


from . import views

app_name = 'asim'
urlpatterns = [
    # ex: 
    url(r'^$', views.index, name='index'),
    url(r'browse/$', views.browse, name='browse'),
    url(r'tgf/$', views.tgf, name='tgf'),
    url(r'orbitdisplay/$', views.orbitdisplay, name='orbitdisplay'),
    url(r'your_location/$', views.your_location, name='your_location'),

    # ex: 
    url(r'^(?P<obsid>[0-9]+)/$', views.detail, name='detail'),
    # ex: 
    url(r'^(?P<obsid>[0-9]+)/results/$', views.results, name='results'),
    # ex: 
    url(r'^(?P<obsid>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'search/$', views.search, name='search'),
    url(r'name/$', views.get_name, name='name'),
    url(r'^location/$', views.location, name='location'),
    url(r'^location/thanks/$', views.thanks, name='thanks'),
] 
