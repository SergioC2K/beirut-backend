from asyncio import Event

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from beirutAdmin.models import Gallery, Locations, Reservations, SpecialEvents, Menus, Categories, BeirutVideos
from beirutAdmin.serializers import GallerySerializer, LocationsSerializer, ReservationsSerializer, \
    SpecialEventsSerializer, MenusSerializer, CategoriesSerializer, GalleryVideoSerializer


# Locations
class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationsSerializer
    queryset = Locations.objects.all()


# Reservations
class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationsSerializer
    queryset = Reservations.objects.all()


class EventView(viewsets.ModelViewSet):
    serializer_class = SpecialEventsSerializer
    queryset = SpecialEvents.objects.all()


class MenuView(viewsets.ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menus.objects.all()


class MenuCategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class GalleryView(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class GalleryVideoView(viewsets.ModelViewSet):
    serializer_class = GalleryVideoSerializer
    queryset = BeirutVideos.objects.all()


# Users
@api_view(['POST'])
def login(request):
    return Response({'message': 'Prueba'})
