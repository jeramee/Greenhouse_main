from django.contrib import admin

# Register your models here.

from .models import Greenhouse, Device, Vegetable, Fruit, Herb

admin.site.register(Greenhouse)

admin.site.register(Device)

admin.site.register(Fruit)

admin.site.register(Herb)

admin.site.register(Vegetable)

