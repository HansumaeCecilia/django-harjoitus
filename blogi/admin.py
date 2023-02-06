from django.contrib import admin

from .models import Postaus

# Luo model-admin
@admin.register(Postaus)
class PostausAdmin(admin.ModelAdmin):
    pass
