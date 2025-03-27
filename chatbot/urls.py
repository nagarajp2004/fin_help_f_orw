from django.urls import path
from .views import financial_api

urlpatterns = [
    path('api/', financial_api, name='financial_api'),
]