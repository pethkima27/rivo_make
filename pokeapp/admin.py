from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Card

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'foto', 'bio', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('foto', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('foto', 'bio')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Card)
