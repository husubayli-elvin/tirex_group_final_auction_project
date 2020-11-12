from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('products/', views.BrowseListView.as_view(), name='browse-list'),
    path('streetwear/', views.StreetwearView.as_view(), name='streetwear-page'),
    path('about/', views.AboutUsView.as_view(), name='about-page'),
    path('help/', views.HelpView.as_view(), name='help-page'),
    path('product/<slug:slug>', views.SingleView.as_view(), name='product-detail'),
    path('sell_it/<slug:slug>', views.SellProductView.as_view(), name='sell-product'),
    path('sell/<slug:slug>', views.SellSizeProductView.as_view(), name='sell-size-product'),
    path('buy_it/<slug:slug>', views.BuyProductView.as_view(), name='buy-product'),
    path('buy/<slug:slug>', views.BuySizeProductView.as_view(), name='buy-size-product'),
]