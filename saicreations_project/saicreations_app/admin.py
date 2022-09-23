from django.contrib import admin
from .models import Newsletter, Product, Admin
# Register your models here.

admin.site.register(Newsletter)
admin.site.register(Product)
admin.site.register(Admin)