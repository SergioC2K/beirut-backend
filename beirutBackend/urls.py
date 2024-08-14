from django.contrib import admin
from django.urls import path, include
from beirutBackend import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('beirutAdmin.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
