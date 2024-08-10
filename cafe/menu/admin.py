from django.contrib import admin
from .models import Menu
from .models import Food

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'description',)

class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('name', 'description','menu', 'order')



admin.site.register(Menu, MenuAdmin)


admin.site.register(Food, FoodAdmin)

