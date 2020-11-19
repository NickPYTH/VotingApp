from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from voting.views import index, stats_login

urlpatterns = [
    path("", index, name="main"),
    path("admin/", admin.site.urls),
    path("stats_login/", stats_login, name="stats"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
