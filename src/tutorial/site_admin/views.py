from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from tutorial.master.models import Category
from tutorial.site_admin.forms import CategoryCreateForm, CategoryEditForm
from tutorial.views import AdminLoginRequiredMixin


class CategoryCreateView(AdminLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('site_admin:category_list')
    template_name = "site_admin/category/create.html"
    success_message = "登録しました。"


class CategoryListView(AdminLoginRequiredMixin, ListView):
    model = Category
    template_name = "site_admin/category/list.html"
    context_object_name = "category_list"
    paginate_by = 10


class CategoryEditView(AdminLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    success_url = reverse_lazy('site_admin:category_list')
    pk_url_kwarg = 'category_id'
    template_name = "site_admin/category/edit.html"
    success_message = "修正しました。"

