from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'realgraph.views.home', name='home'),
    url(r'^graph/', 'realgraph.views.graph', name='graph'),
    # url(r'^evsgraph/', include('evsgraph.foo.urls')),
    url(r'^airquality/', 'realgraph.views.airquality', name='airquality'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
