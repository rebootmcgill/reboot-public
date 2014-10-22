from django.conf.urls import patterns, include, url
from django.contrib import admin
from publicreboot.views import RequestCreate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reboot.views.home', name='home'),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^request/$', RequestCreate.as_view()),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/home/'}, name='home'),
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^recycling/$', 'flatpage', {'url': '/recycling/'}, name='recycling'),
    url(r'^request/thanks/$', 'flatpage', {'url': '/request/thanks/'}, name='thanks'),
)

