from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', test, name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^new/$', test, name='new'),
    url(r'^popular/$', test, name='popular'),
    url(r'^ask/', test, name='ask'),
    url(r'^question/(?P<question_id>[0-9]+)/$', test, name='question_detail'),
    url(r'^signup/$', test, name='signup'),
    url(r'^login/$', test, name='login'),
    url(r'^$', test, name='index'),
)
