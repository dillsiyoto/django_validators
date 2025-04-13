from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="", view=include("clients.urls")),
    path(route="posts/", view=include("posts.urls")),
]