from django.contrib import admin
from .models import User, UserAddress


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'email', 'password', 'language', 'user_status']


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'city', 'district', 'ward', 'street', 'user_id']