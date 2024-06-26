from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', 'catalog')),
    path('bloging/', include('bloging.urls', 'bloging')),
    path('users/', include('users.urls', 'users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
