from django.conf.urls import url
from tutorial.todo.views import ToDoUserCreateView, ToDoCreateView,\
     ToDoListView, ToDoDetailView, ToDoEditView

urlpatterns = [
    url(r"^$", ToDoListView.as_view(), name="list"),
    url(r"^(?P<todo_id>\d+)/$", ToDoDetailView.as_view(), name="detail"),
    url(r"^(?P<todo_id>\d+)/edit$", ToDoEditView.as_view(), name="edit"),
    url(r"^create/$", ToDoCreateView.as_view(), name="create"),
    url(r"^user/create/$", ToDoUserCreateView.as_view(), name="user_create"),
]
