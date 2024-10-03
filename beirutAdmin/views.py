from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from beirutAdmin import models, serializers
from django.shortcuts import get_object_or_404
from django.http import Http404


# Locations
class LocationView(viewsets.ModelViewSet):
    serializer_class = serializers.LocationsSerializer
    queryset = models.Locations.objects.all()


class ReservationView(viewsets.ModelViewSet):
    serializer_class = serializers.ReservationsSerializer
    queryset = models.Reservations.objects.all()


class ReservationStatusView(viewsets.ModelViewSet):
    serializer_class = serializers.ReservationStatusSerializer
    queryset = models.ReservationStatus.objects.all()


class EventView(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialEventsSerializer
    queryset = models.SpecialEvents.objects.all()


class MenuView(viewsets.ModelViewSet):
    serializer_class = serializers.MenusSerializer

    def get_queryset(self):
        queryset = models.Menus.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class MenuCategoriesView(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()


class GalleryView(viewsets.ModelViewSet):
    serializer_class = serializers.GallerySerializer
    queryset = models.Gallery.objects.all()


class GalleryVideoView(viewsets.ModelViewSet):
    serializer_class = serializers.GalleryVideoSerializer
    queryset = models.BeirutVideos.objects.all()


# Users
@api_view(['POST'])
def login(request):
    try:
        user = get_object_or_404(models.UserAdmin, user_name=request.data["username"])
    except Http404:
        return Response({"error": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(request.data["password"]):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = serializers.UserSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def available_hours_view(request):

    date = request.query_params.get('date')
    parsed_date = datetime.strptime(date, '%Y-%m-%d')
    open_hour = datetime.combine(parsed_date, datetime.min.time().replace(hour=17))
    close_hour = datetime.combine(parsed_date, datetime.min.time().replace(hour=21, minute=30))
    print(open_hour, close_hour)
    #
    # booking_day = models.Reservations.objects.filter(date=date).order_by('date')
    #
    # available_hours = []
    # current_hour = open_hour
    available_hours = [
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00"]
    return Response({'available_hours': available_hours})
