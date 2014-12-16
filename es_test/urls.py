from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/', include('haystack.urls')),
    url(r'^blog/(?P<pk>[0-9]+)', 'blog.views.detail', name='blog_detail'),
)
