from django.conf import settings 
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^depotapp/', include('depotapp.urls')),
    url(r'^crf/', include('crfapp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)