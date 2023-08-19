from django.contrib import admin
from .models import Form

# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    # add - in front of name to reverse order
    ordering = ("first_name", )
    # Set to read only
    readonly_fields = ("occupation", )

admin.site.register(Form, FormAdmin)