from django.contrib import admin

from .models import CustomUser, Fan, Presentation, Darslik, IshReja

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "phone"]
    list_display_links = ["id", "username","first_name"]
    list_editable = ["phone"]
    list_filter = ["is_superuser"]
    search_fields = ["first_name", "last_name", "phone", "username"]
    list_per_page = 30

class FanAdmin(admin.ModelAdmin):
    list_display = ["name", "sinf", "guruh"]
    list_display_links = ["name"]
    search_fields = ["name", "sinf", "guruh"]
    list_filter = ["guruh"]
    list_per_page = 30

class PresentationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "fan__name", "fan__sinf", "fan__guruh"]
    list_display_links = ["id", "name"]
    list_filter = ["price", "fan__name", "fan__sinf", "fan__guruh", "chorak"]
    search_fields = ["name", "fan__name", "fan__sinf"]
    list_per_page = 30

class DarslikAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "fan__name", "fan__sinf", "fan__guruh"]
    list_display_links = ["id", "name"]
    list_filter = ["fan__name", "fan__sinf", "fan__guruh"]
    search_fields = ["name", "fan__name", "fan__sinf"]
    list_per_page = 30

class IshRejaAdmin(admin.ModelAdmin):
    list_display = ["id", "fan__name", "fan__sinf", "fan__guruh", "chorak"]
    list_display_links = ["id"]
    list_filter = ["fan__name", "fan__sinf", "fan__guruh", "chorak"]
    search_fields = ["fan__name", "fan__sinf", "chorak"]
    list_per_page = 30

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Darslik, DarslikAdmin)
admin.site.register(IshReja, IshRejaAdmin)
