from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'details', 'order_date', 'status', 'change_status_buttons')
    list_filter = ('status',)
    fields = ('user', 'details') 
    list_editable = ('status', 'details')  # הוספת שדות לעריכה ישירה

    def change_status_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}">התקבלה</a>&nbsp;'
            '<a class="button" href="{}">אושרה</a>&nbsp;'
            '<a class="button" href="{}">הגיעה לחנות</a>',
            reverse('mark_received', args=[obj.id]),
            reverse('mark_approved', args=[obj.id]),
            reverse('mark_arrived', args=[obj.id]),
        )
    change_status_buttons.short_description = 'שינוי סטטוס'
    change_status_buttons.allow_tags = True

admin.site.register(Order, OrderAdmin)