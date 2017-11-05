from views import searchAPI
from django.conf.urls import url

urlpatterns = [
    url(r'search', searchAPI, name="search")
]