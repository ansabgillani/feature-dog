from django.urls import path
from posts.views.posts import (
    PostListCreateView,
    PostDetailView,
    UpvoteListCreateView,
)
from posts.views.comments import (
    CommentRetrieveView,
    CommentListCreateView,
    CommentUpvoteListCreateView
)
from posts.views.tags import TagListCreateView

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
         CommentRetrieveView.as_view(), name='comment_create_view'),
    # Comment Create View for a particular post

    path('api/<organization_slug>/posts/<int:post_pk>/comments/<int:comment_pk>/upvotes',
         CommentUpvoteListCreateView.as_view(), name='comment_upvote_list_create_view'),
    # Comment Upvote View for a particular comment

    path('api/<organization_slug>/tags',
         TagListCreateView.as_view(), name='tags_list_create_view'),
    # Comment Upvote View for a particular comment

]
