from django.conf.urls.defaults import patterns, include, url
#import horizon
#from .views import (NetworkTopology, JSONView)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'network_topology.views.home', name='home'),
    # url(r'^network_topology/', include('network_topology.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
 #   url(r'^$', NetworkTopology.as_view(), name='index'),
   # url(r'^$', NetworkTopology.as_view(), name='index'),
    #url(r'^json$', JSONView.as_view(), name='json'),
 #   url(r'', include(horizon.urls), name='horizon'),
    url(r'^$','curation.demitase.views.timeline'),
#    url(r'^timeline/$', 'curation.demitase.views.timeline'),
)
