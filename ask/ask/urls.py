from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^new/$', 'ask.views.home', name='new'),
    #url(r'^popular/$', 'ask.views.home', name='popular'),
    #url(r'^ask/$', 'ask.views.home', name='ask'),
    url(r'^question/(?P<question_id>[0-9]+)/$', test, name='question_detail'),
    #url(r'^signup/$', 'ask.views.home', name='signup'),
    #url(r'^login/$', 'ask.views.home', name='login'),
    #url(r'^$', 'ask.views.home', name='index'),
)
