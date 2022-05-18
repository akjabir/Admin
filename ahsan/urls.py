from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('job.urls')),
    path("/", include('job.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


