from django.contrib import admin
from .models import Friendship

# Register your models here.
class AdminFriendship(admin.ModelAdmin):
    list_display = ['user','friend','status','timestamp']

admin.site.register(Friendship, AdminFriendship)
