from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, MainLoginView, ForgetPasswordView, ResetPasswordView, ProfileView, BuyingView, CopListView, PortfolioView, SellingView, SettingView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name = 'password-reset-confirm'),
    path('user-profile/<int:pk>', ProfileView.as_view(), name='user-profile'),
    path('user-profile/<int:pk>/buyings', BuyingView.as_view(), name='buyings'),
    path('user-profile/<int:pk>/cop-list', CopListView.as_view(), name='cop-list'),
    path('user-profile/<int:pk>/portfolio', PortfolioView.as_view(), name='portfolio'),
    path('user-profile/<int:pk>/selling', SellingView.as_view(), name='selling'),
    path('user-profile/<int:pk>/settings', SettingView.as_view(), name='settings'),
]