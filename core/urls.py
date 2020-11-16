from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('product/<int:pk>', views.SingleView.as_view(), name='product-detail'),
    path('sell/', views.SellView.as_view(), name='sell'),
    path('sell/<int:pk>', views.SellSingleView.as_view(), name='sell-detail'),
    path('sell/<int:pk>/confirm', views.SellConfirmationView.as_view(), name='sell-detail-confirm'),

]