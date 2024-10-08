from django.urls import path, include
from rest_framework import routers
from beirutAdmin import views

router = routers.DefaultRouter()
router.register(r'location', views.LocationView, basename='location')
router.register(r'reservation', views.ReservationView, basename='reservation')
router.register(r'reservation-status', views.ReservationStatusView, basename='reservation-status')
router.register(r'event', views.EventView, basename='event')
router.register(r'menu', views.MenuView, basename='menu')
router.register(r'menu-categories', views.MenuCategoriesView, basename='menu-categories')
router.register(r'gallery', views.GalleryView, basename='gallery')
router.register(r'gallery-videos', views.GalleryVideoView, basename='gallery-videos')

urlpatterns = [
    path('v1/login', views.login, name='login'),
    path('v1/reservation-hours', views.available_hours_view, name='reservation-hours'),
    path('v1/', include(router.urls)),
]
