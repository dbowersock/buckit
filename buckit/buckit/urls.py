from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buckit.views.home', name='home'),
    # url(r'^buckit/', include('buckit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/(?P<request_id>\d+)/$', 'foundation.views.request_detail'),
    url(r'^requests/', 'foundation.views.requests_index'),
    url(r'^', 'foundation.views.index'),
)
