from django.urls import path

from . import views

app_name = 'itemsdb'

urlpatterns = [

    # Singular Paths
    path('', views.IndexView.as_view(), name='index'),
]
