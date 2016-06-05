from django.conf.urls import url
from tutorial.site_admin.views import CategoryCreateView, CategoryListView,\
     CategoryEditView

urlpatterns = [
    url(r"^category/$", CategoryListView.as_view(), name="category_list"),
    url(r"^category/(?P<category_id>\d+)/$", CategoryEditView.as_view(), name="category_edit"),
    url(r"^category/create/$", CategoryCreateView.as_view(), name="category_create"),
]
