from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('product/<int:pk>', views.SingleView.as_view(), name='product-detail'),
    
]