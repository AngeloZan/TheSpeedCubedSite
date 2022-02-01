from django.contrib import admin
from website.models import FeedbackModel

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'message', 'send_date')
    search_fields = ('name', 'contact', 'message', 'send_date')
    readonly_fields = ('name', 'contact', 'message', 'send_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(FeedbackModel, FeedbackAdmin)