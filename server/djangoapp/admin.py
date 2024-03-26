from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
# class CarModelInline(admin.StackedInline):
#     model = CarMake 
#     extra = 5
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'year']
    # inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
