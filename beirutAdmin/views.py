from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from beirutAdmin import models, serializers
from django.shortcuts import get_object_or_404


# Locations
class LocationView(viewsets.ModelViewSet):
    serializer_class = serializers.LocationsSerializer
    queryset = models.Locations.objects.all()


# Reservations
class ReservationView(viewsets.ModelViewSet):
    serializer_class = serializers.ReservationsSerializer
    queryset = models.Reservations.objects.all()


class EventView(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialEventsSerializer
    queryset = models.SpecialEvents.objects.all()


class MenuView(viewsets.ModelViewSet):
    serializer_class = serializers.MenusSerializer

    def get_queryset(self):
        queryset = models.Menus.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if id is not None:
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
    
    user = get_object_or_404(models.UserAdmin,user_name = request.data["username"])

    if not user.check_password(request.data["password"]):
        return Response({"error": "Invalid password"},status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = serializers.UserSerializer(instance=user)

    return Response({'token': token.key,'user':serializer.data},status=status.HTTP_200_OK)
