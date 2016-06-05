from django.conf.urls import url
from tutorial.todo.views import ToDoUserCreateView

urlpatterns = [
    url(r"^user/create/$", ToDoUserCreateView.as_view(), name="user_create"),
]
