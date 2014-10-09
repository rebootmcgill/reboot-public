from django.conf.urls import patterns, url


urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/home/'}, name='home'),
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)
