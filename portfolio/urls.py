from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portfolio.portapp.views.home', name='home'),
    url(r'^bio/', 'portfolio.portapp.views.bio', name='bio'),
    url(r'^projects/', 'portfolio.portapp.views.projects', name='projects'),
    url(r'^contact/', 'portfolio.portapp.views.contact', name='contact'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)
