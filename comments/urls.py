from django.urls import path

from comments.views import (
    CommentsView
)


urlpatterns = [
    path(route = 'comments/', view = CommentView.as_view(), name = 'comments')
]