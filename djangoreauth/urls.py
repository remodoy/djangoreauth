from django.conf.urls import patterns, url

urlpatterns = patterns('',
     url(r'login/?$', 'djangoreauth.views.reauth_login', name='reauth_login'),
)
