from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CartItem)
admin.site.register(Restaurant)
admin.site.register(Question)
admin.site.register(Preference)