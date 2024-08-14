from rest_framework import serializers

from .models import Gallery, Menus, SpecialEvents, Locations, Reservations, Categories, BeirutVideos


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'


class SpecialEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialEvents
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeirutVideos
        fields = '__all__'
