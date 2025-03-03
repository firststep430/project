from django.urls import path
from .views import add_ingredient

urlpatterns = [
    path('add_ingredient/', add_ingredient, name='add_ingredient'),
]
