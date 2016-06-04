from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.shortcuts import render


admin.autodiscover()

urlpatterns = [
    url(r'^$', lambda request: render(request, "index.html"), name="index"),
    url(r'^todo/', include('tutorial.todo.urls', namespace="todo")),
    url(r'^master/', include('tutorial.master.urls', namespace="master")),
    url(r'^admin/', include('tutorial.site_admin.urls', namespace="site_admin")),
    url(r'^admin/native/', include(admin.site.urls)),

    url(r'^login/$', login, name="login", kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout, name="logout", kwargs={"next_page": 'index'}),
]
