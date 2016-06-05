from django.conf.urls import url
from tutorial.todo.views import ToDoUserCreateView, ToDoCreateView,\
     ToDoListView

urlpatterns = [
    url(r"^$", ToDoListView.as_view(), name="list"),
    url(r"^create/$", ToDoCreateView.as_view(), name="create"),
    url(r"^user/create/$", ToDoUserCreateView.as_view(), name="user_create"),
]
