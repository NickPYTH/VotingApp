from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from voting.views import index, get_stats, users_stats, admin_stats

urlpatterns = [
    path("", index, name="main"),
    path("admin/", admin.site.urls),
    path("users_stats/", users_stats, name="users_stats"),
    path("admin_stats/", admin_stats, name="admin_stats"),
    path("download_stats/", get_stats, name="download"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
