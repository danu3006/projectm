from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls', namespace='api')),
    path('', include('itemsdb.urls', namespace='itemsdb')),
    path('admin/', admin.site.urls),
]
