from django.contrib import admin
from .models import Gallery

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["name", "upload_date"]

    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)
