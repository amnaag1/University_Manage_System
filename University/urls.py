from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from . import settings
from django.conf.urls.static import static
from pathlib import Path

urlpatterns = [
    path('', user_views.home, name='home'),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=Path(settings.BASE_DIR) / 'static')
