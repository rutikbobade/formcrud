from django.contrib import admin
from formcrudapp.models import crud
# Register your models here.

@admin.register(crud)
class crudAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
    