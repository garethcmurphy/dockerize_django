from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^asim/', include('asim.urls', namespace='asim')),
    url(r'^admin/', include(admin.site.urls)),
)
