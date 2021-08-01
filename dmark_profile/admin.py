from django.contrib import admin
from .models.employee import Employee
from .models.contact import Contact_details
# Register your models here.

class Show_employees(admin.ModelAdmin):
    list_display = ['applied_for','first_name_taken','last_name_taken',
                    'phone_number_taken','email_id_taken','description_taken']

class show_sended_message(admin.ModelAdmin):
    list_display = ['name','phone_no','email','subject','message']


admin.site.register(Employee,Show_employees)
admin.site.register(Contact_details,show_sended_message)

