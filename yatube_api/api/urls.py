from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views as api_views

router = SimpleRouter()

router.register('posts', api_views.PostViewSet)
router.register('groups', api_views.GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    api_views.CommentViewSet,
    basename='comments'
)
router.register('follow', api_views.FollowViewSet)

app_name = 'api'

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
