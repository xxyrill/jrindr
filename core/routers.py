from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()

# User router
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'post', PostViewSet, basename='post')

# Post router for nested comments
post_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
post_router.register(r'comment', CommentViewSet, basename='post-comments')

urlpatterns = [
    *router.urls,
    *post_router.urls
]