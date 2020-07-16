from django.urls import path, include
from microblog_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserProfileViewSet)
router.register("blog", views.BlogViewSet)
router.register("comment", views.CommentViewSet)


urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
    path("", include(router.urls))
]
