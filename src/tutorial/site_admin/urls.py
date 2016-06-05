from django.conf.urls import url
from tutorial.site_admin.views import CategoryCreateView

urlpatterns = [
    url(r"^category/create/$", CategoryCreateView.as_view(), name="category_create"),
]
