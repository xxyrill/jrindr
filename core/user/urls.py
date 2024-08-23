from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.comment.viewsets import CommentViewSet
from core.post.viewsets import PostViewSet
from core.routers import post_router
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='users') # user list route http://127.0.0.1:8000/api/user
# ang user sa taas kay endpoints na, prefix means sa tumoy nabutang
# parehas ani, url http://127.0.0.1:8000/api/user
router.register(r'register', RegisterViewSet, basename='auth-register')
# url http://127.0.0.1:8000/api/auth/register
router.register(r'login', LoginViewSet, basename='auth-login')
# url http://127.0.0.1:8000/api/auth/login/
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
# url http://127.0.0.1:8000/api/auth/refresh/
router.register(r'post', PostViewSet, basename='post')
# url http://127.0.0.1:8000/api/post/

# Nested routers for comments under posts
post_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
post_router.register(r'comment', CommentViewSet, basename='post-comment')

# ang UserViewSet kay gi import gkan sa viewsets.py tapos
# gi register sa line 6

# ang basename kay optional ra, pero good practice nga naay basename
# kay it helps for readability

urlpatterns = [
    path('', include(router.urls)),     # kay daghan naman imng url sa taas, dapat
    path('', include(post_router.urls)),                                    # ingon anion sya
]