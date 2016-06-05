from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from tutorial.todo.models import ToDoUser, ToDo
from tutorial.todo.forms import ToDoUserCreateForm, ToDoCreateForm
from tutorial.views import LoginRequiredMixin


class ToDoUserCreateView(SuccessMessageMixin, CreateView):
    model = ToDoUser
    form_class = ToDoUserCreateForm
    success_url = reverse_lazy('index')
    template_name = "todo/user_create.html"
    success_message = "登録しました。"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


class ToDoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ToDo
    form_class = ToDoCreateForm
    success_url = reverse_lazy('index')
    template_name = "todo/create.html"
    success_message = "登録しました。"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs

