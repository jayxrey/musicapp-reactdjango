from django.contrib import admin

# Register your models here.
from .models import Artists

class ArtistsAdmin(admin.ModelAdmin):
    list_display = ('song', 'artist', 'album','genre','year')

admin.site.register(Artists, ArtistsAdmin)
