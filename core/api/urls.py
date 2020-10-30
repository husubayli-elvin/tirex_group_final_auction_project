from django.urls import path
from .views import SearchProductAPI

app_name = 'search_api'

urlpatterns = [
    path('search/', SearchProductAPI.as_view(), name='search'),
]