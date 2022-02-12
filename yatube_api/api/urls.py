from django.urls import include, path

from rest_framework.routers import SimpleRouter

from . import views

router_v1 = SimpleRouter()

router_v1.register('v1/posts', views.PostViewSet)
router_v1.register('v1/groups', views.GroupViewSet)
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment'
)
router_v1.register(
    'v1/follow',
    views.FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]
