from django.urls import path

from . import api

app_name = 'api'

urlpatterns = [

    # Item API Endpoints
    path('items/active/', api.ActiveItemListAPIHandler.as_view(), name='active-item-list'),
]
