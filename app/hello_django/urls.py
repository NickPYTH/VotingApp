from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from voting.views import vote_list, index, stats

urlpatterns = [
    path("", index, name="main"),
    path("admin/", admin.site.urls),
    path("stats/", stats, name="stats"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
