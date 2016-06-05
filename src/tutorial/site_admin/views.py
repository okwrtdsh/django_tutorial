from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from tutorial.master.models import Category
from tutorial.site_admin.forms import CategoryCreateForm
from tutorial.views import AdminLoginRequiredMixin


class CategoryCreateView(AdminLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('index')
    template_name = "site_admin/category/create.html"
    success_message = "登録しました。"

