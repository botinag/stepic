from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()
from qa.views import (
    test, new_questions, popular_questions, question_detail, ask, answer)


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', test, name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^new/$', test, name='new'),
    url(r'^popular/$', popular_questions, name='popular'),
    url(r'^ask/', ask, name='ask'),
    url(r'^answer/', answer, name='answer'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail,
        name='question_detail'),
    url(r'^signup/$', test, name='signup'),
    url(r'^login/$', test, name='login'),
    url(r'^$', new_questions, name='index'),
)
