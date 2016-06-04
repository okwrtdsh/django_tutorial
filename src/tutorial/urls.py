from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^todo/', include('tutorial.todo.urls', namespace="todo")),
    url(r'^master/', include('tutorial.master.urls', namespace="master")),
    url(r'^admin/', include('tutorial.site_admin.urls', namespace="site_admin")),
    url(r'^admin/native/', include(admin.site.urls)),
]
