from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Gallery, BeirutVideos, SpecialEvents

admin.site.register(Gallery)
admin.site.register(SpecialEvents)
admin.site.register(BeirutVideos)
