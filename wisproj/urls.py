
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from django.conf.urls.static import static
from wisapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('wisapp.urls')),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
