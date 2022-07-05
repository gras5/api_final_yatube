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
router.register(
    'follow',
    api_views.FollowViewSet,
    basename='follows'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
