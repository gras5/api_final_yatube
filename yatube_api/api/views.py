from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import (
    GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
)

from posts.models import Comment, Follow, Group, Post
from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        return Comment.objects.filter(
            post__pk=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )

        serializer.save(
            post=post,
            author=self.request.user
        )


class FollowViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = (
        '=user__username',
        '=following__username'
    )

    def get_queryset(self):
        return Follow.objects.filter(
            user=self.request.user.pk
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
