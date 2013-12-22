from django.conf.urls import patterns, include, url
from banana.views import hello, current_datetime, hours_ahead
# from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^current-time/$', current_datetime),
                       url(r'^time/$', current_datetime),
                       url(r'^time/dateapp/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
                       # Examples:
                       # url(r'^$', 'banana.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
)
