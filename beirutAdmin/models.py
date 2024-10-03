from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, user_full_name=None, user_name=None, **extra_fields):
        if not email:
            raise ValueError('The email must be provided')
        if not password:
            raise ValueError('The password must be provided')

        user = self.model(
            email=self.normalize_email(email),
            user_full_name=user_full_name,
            user_name=user_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, user_full_name=None, user_name=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, user_full_name, user_name, **extra_fields)

    def create_superuser(self, email, password, user_full_name=None, user_name=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, user_full_name, user_name, **extra_fields)


class UserAdmin(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    user_name = models.CharField(max_length=255, unique=True)
    user_full_name = models.CharField(max_length=255)
    user_login = models.CharField(max_length=100, unique=True)

    user_created = models.DateTimeField(auto_now_add=True)
    user_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'user_full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.user_name

    def get_user_permissions(self, obj=None):
        return self.user_permissions.all()


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.ImageField(max_length=500, upload_to='gallery')
    name = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_date(self):
        return self.status


class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    mapLocation = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_address(self):
        return self.address

    def get_mapLocation(self):
        return self.mapLocation

    def get_id(self):
        return self.id


class ReservationStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)


class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=500)
    client_name = models.CharField(max_length=500)
    number_guests = models.IntegerField(default=0)
    phoneNumber = models.CharField(max_length=500)
    special_request = models.CharField(max_length=500, blank=True, null=True)
    status = models.ForeignKey(ReservationStatus, on_delete=models.CASCADE)

    def get_guests(self):
        return self.number_guests

    def get_name(self):
        return self.client_name

    def get_email(self):
        return self.email

    def reservation_finished(self):
        return self.status

    def is_confirmed(self):
        available_reservations = Reservations.objects.filter(status=self.status)


class SpecialEvents(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    event_name = models.CharField(max_length=500)
    event_description = models.CharField(max_length=500)
    additional_info = models.CharField(max_length=500, blank=True, null=True)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=False)
    image = models.ImageField(max_length=500, upload_to='special-events')

    def __str__(self):
        return self.event_name

    def get_date(self):
        return self.date

    def get_event_location(self):
        return self.event_location

    def get_event_name(self):
        return self.event_name

    def get_event_description(self):
        return self.event_description

    def get_additional_info(self):
        return self.additional_info

    def get_hour(self):
        return self.hour

    def get_status(self):
        return self.status


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


class Menus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description


class BeirutVideos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    video_url = models.FileField(max_length=500, upload_to='videos')
    status = models.BooleanField(default=False)
