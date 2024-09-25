from rest_framework import serializers
from . import models


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'


class MenusSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = models.Menus
        fields = '__all__'


class SpecialEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpecialEvents
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Locations
        fields = '__all__'


class ReservationsSerializer(serializers.ModelSerializer):
    # location = serializers.CharField(source='location.name', read_only=True)
    # location_id = serializers.CharField(source='location.id', read_only=True)
    class Meta:
        model = models.Reservations
        fields = '__all__'


class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BeirutVideos
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAdmin
        fields = ['email', 'user_name', 'user_full_name', 'user_created', 'user_updated', 'is_active', 'is_staff',
                  'is_superuser']
