from django.contrib import admin
from .models import Reptile

# Register your models here.
class ReptileAdmin(admin.ModelAdmin):
    list_display = ("pk","nom","nomEspece","ordre","age","poids","user")

admin.site.register(Reptile,ReptileAdmin)
