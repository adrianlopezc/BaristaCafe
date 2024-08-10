from django.contrib import admin
from django.urls import path, include
from core.urls import core_urlpatterns
from menu.urls import menu_urlpatterns
from django.conf import settings
from django.conf.urls.static import static   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('menu/', include(menu_urlpatterns)),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)