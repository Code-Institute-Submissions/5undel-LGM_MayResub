from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('order_history/<membership_number>', views.order_history, name='order_history'),
]