
from django.contrib import admin
from django.urls import path, include


import adminapp.urls
import usersapp.urls


# to display images from database
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from . import settings

urlpatterns = [
    path('admin/',admin.site.urls),
    path('adminsapp/',include(adminapp.urls)),
    path('',include(usersapp.urls)),


]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)