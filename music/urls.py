from django.urls import path, include
from .views import LandingPageAPIView, ArtistAPIView, ArtistDetailAPIView, AlbomDetailAPIView, SongsViewAPIViewSet, AlbomAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("songs", viewset=SongsViewAPIViewSet)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artist/', ArtistAPIView.as_view(), name="artists"),
    path('artist/<int:id>/', ArtistDetailAPIView.as_view(), name="artist-detail"),
    path("", include(router.urls)),
    path('albom/', AlbomAPIView.as_view(), name="alboms"),
    path('albom/<int:id>/', AlbomDetailAPIView.as_view(), name="albom-detail"),
]