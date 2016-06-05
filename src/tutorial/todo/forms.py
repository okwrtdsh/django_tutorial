from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from django_cbv_utils.forms import SetFromControlMixin
from tutorial.todo.models import ToDoUser


class ToDoUserCreateForm(UserCreationForm, SetFromControlMixin):
    email = forms.EmailField(label="メールアドレス", required=True)
    username = forms.RegexField(
        label="ユーザー名",
        max_length=15,
        regex=r'^[a-zA-Z0-9]+$',
        error_messages={'invalid': "半角英数15字以内で入力してください。"})

    class Meta:
        model = ToDoUser
        fields = [
            "username",
            "password1",
            "password2",
            "handle_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        todouser = super().save(commit)
        if commit:
            user = authenticate(
                username=self.cleaned_data["username"],
                password=self.cleaned_data["password1"])
            if user is not None and user.is_active:
                    login(self.request, user)
        return todouser

