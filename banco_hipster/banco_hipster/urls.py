from django.conf.urls import url, include, patterns
from django.contrib import admin
from banco_hipster.views import RegistrarUsuarioView
from banco_hipster import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$','django.contrib.auth.views.login', {'template_name' : 'login.html'}, name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login', {'login_url' : '/login/'}, name="logout"),
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar')
]
