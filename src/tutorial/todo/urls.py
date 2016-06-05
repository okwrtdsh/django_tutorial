from django.conf.urls import url
from tutorial.todo.views import ToDoUserCreateView, ToDoCreateView

urlpatterns = [
    url(r"^create/$", ToDoCreateView.as_view(), name="create"),
    url(r"^user/create/$", ToDoUserCreateView.as_view(), name="user_create"),
]
