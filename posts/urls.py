from django.urls import path, include
from posts.views import (
    PostListCreateView,
    PostDetailView,
    CommentRetriveView,
    CommentListCreateView,
    UpvoteListCreateView,
    CommentUpvoteListCreateView
)

urlpatterns = [
    # path('', include(router.urls)),
    path('api/<organization_slug>/posts', PostListCreateView.as_view(),
         name='post_list_view'),  # Post List View
    path('api/<organization_slug>/posts/<int:pk>',
         PostDetailView.as_view(), name='post_detail_view'),
    # Post List View

    path('api/<organization_slug>/posts/<int:post_pk>/upvote',
         UpvoteListCreateView.as_view(), name='post_detail_view'),
    # Post List View

    path('api/<organization_slug>/posts/<int:post_pk>/comments', CommentListCreateView.as_view(),
         name='comment_create_view'),  # Comment Create View for a particular post

    path('api/<organization_slug>/posts/<int:post_pk>/comments/<int:comment_pk>',
         CommentRetriveView.as_view(), name='comment_create_view'),
    # Comment Create View for a particular post

    path('api/<organization_slug>/posts/<int:post_pk>/comments/<int:comment_pk>/upvotes',
         CommentUpvoteListCreateView.as_view(), name='comment_upvote_list_create_view'),
    # Comment Upvote View for a particular comment
]
