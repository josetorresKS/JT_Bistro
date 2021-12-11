from django.urls import path
from . import views

urlpatterns = [
    path('https://jtbistro-backend.herokuapp.com', views.ItemList.as_view(), name='item_list'),
]
