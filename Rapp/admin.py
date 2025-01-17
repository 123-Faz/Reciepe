from django.contrib import admin
from .models import Reciepe
# Register your models here.
@admin.register(Reciepe)
class ReciepeAdmin(admin.ModelAdmin):
    list_display = ('Reciepe_name', 'Reciepe_description' ,'Reciepe_image')







