from django.contrib import admin
from service.models import Contact
from service.models import Department
from service.models import DoctorDetails

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=("full_name","email_id","subject","mob_num","message")

class DepartmentAdmin(admin.ModelAdmin):
    list_display=("department_name",)
    

class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display=("department_name","name","gender","email_id","mobile_number","edu","department_desc")

admin.site.register(Contact,ContactAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(DoctorDetails,DoctorDetailsAdmin)