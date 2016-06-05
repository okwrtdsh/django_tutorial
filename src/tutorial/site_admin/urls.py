from django.conf.urls import url
from tutorial.site_admin.views import CategoryCreateView, CategoryListView

urlpatterns = [
    url(r"^category/$", CategoryListView.as_view(), name="category_list"),
    url(r"^category/create/$", CategoryCreateView.as_view(), name="category_create"),
]
