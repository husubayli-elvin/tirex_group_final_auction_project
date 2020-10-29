from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('products/', views.BrowseListView.as_view(), name='browse-list'),
    
]