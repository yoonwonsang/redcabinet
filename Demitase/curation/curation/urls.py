from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'curation.views.home', name='home'),
    # url(r'^curation/', include('curation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'curation.views.index'),
    url(r'^login/$', 'curation.views.login'),
    url(r'^logout/$', 'curation.views.logout'),
    # url(r'^main/$', 'curation.demitase.views.main'),
    url(r'^demitase/(?P<curr_demitase>[\w\-]+)/',include('curation.demitase.urls')),
    url(r'^demitase/$',include('curation.demitase.urls')),
    
    #OAuth
    url(r'^oauth/$', 'curation.views.login'),
    url(r'^oauth/get_callback/$', 'curation.views.get_callback'),
    url(r'^oauth/get/$', 'curation.views.Get'),
    
    # Added to serve html

    url(r'^home/(?P<page>\w+).html$', 'curation.demitase.views.serve_html'),
)
