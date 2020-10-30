from django.contrib import admin
from .models import Slider1,Insumos,MisionyVision,Galeria

# Register your models here.
class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10

class Slider1Admin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['ident','imagengaleria']
    search_fields = ['ident']
    list_per_page = 10


admin.site.register(Slider1,Slider1Admin)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(MisionyVision)
admin.site.register(Galeria,GaleriaAdmin)
