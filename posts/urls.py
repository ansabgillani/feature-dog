from django.urls import path
from posts.views.posts import (
    PostListCreateView,
    PostDetailView,
    UpvoteListCreateView,
)
from posts.views.comments import (
    CommentListCreateView,
    CommentUpvoteListCreateView
)
from posts.views.tags import TagListCreateView

urlpatterns = [
    path('api/<organization_slug>/posts', PostListCreateView.as_view(),
         name='post_list_create_view'),
    # Organization Posts List View

    path('api/<organization_slug>/posts/<int:pk>',
         PostDetailView.as_view(), name='post_detail_view'),
    # Organization Post Detail View

    path('api/<organization_slug>/posts/<int:post_pk>/upvote',
         UpvoteListCreateView.as_view(), name='upvote_list_create_view'),
    # Organization Post Upvote List View

    path('api/<organization_slug>/posts/<int:post_pk>/comments',
         CommentListCreateView.as_view(), name='comment_list_create_view'),
    # Organization Post Comment List Create View

    path('api/<organization_slug>/posts/<int:post_pk>/comments/<int:comment_pk>/upvotes',
         CommentUpvoteListCreateView.as_view(), name='comment_upvote_list_create_view'),
    # Organization Post Comment Upvotes List Create View

    path('api/<organization_slug>/tags',
         TagListCreateView.as_view(), name='tag_list_create_view'),
    # Organization Tag List Creatw View

]
