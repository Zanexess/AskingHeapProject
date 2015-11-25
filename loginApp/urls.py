from django.conf.urls import include, url

urlpatterns = [
    url(r'^login$', 'loginApp.views.login', name='login'),
    url(r'^logout$', 'loginApp.views.logout', name='logout'),
    url(r'^register$', 'loginApp.views.register', name='register'),

]
