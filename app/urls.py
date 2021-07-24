from django.urls import path
from . import views

urlpatterns = [
    path('', views.PasswordCreateView.as_view(), name='home'),
    path('edit/<pk>', views.PasswordUpdate.as_view(), name='edit'),
    path('delete/<pk>', views.PasswordDelete.as_view(), name='delete'),
]
