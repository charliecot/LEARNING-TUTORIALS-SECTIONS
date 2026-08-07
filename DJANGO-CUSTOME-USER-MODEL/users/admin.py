from django.contrib import admin
from .models import CustomUser,Student,Vehicle,VehicleRegistration
# Register your models here.
admin.site.site_header='CUSTOME ADMIN PANEL'
admin.site.site_title='custom pannel'


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(VehicleRegistration)
class VehicleRegistrationAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'vehicle', 'registration_date', 'expiry_date')
    list_filter = ('vehicle__brand', 'registration_date')
    search_fields = ('plate_number', 'engine_number', 'vehicle__brand', 'vehicle__model')
    list_editable=('expiry_date',)
    #autocomplete_fields=('',)
    raw_id_fields=('vehicle',)
    #ordering=('-plate_number',)
    list_per_page=2
    def get_ordering(self, request):
       user=request.user
       if user.is_admin:
           return ('plate_number',)
       else:
           return ('-expiry_date',)
        







































class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','matricule','gender','course','capitalised_column')
    list_display_links=( 'matricule',)
    list_editable=('gender','course')
    list_filter=('first_name','gender')
    search_fields=('first_name__startswith',)
    @admin.display(boolean=True ,description='new_name')
    def course_code(self,obj):
        return  False #f'{obj.course}-{obj.matricule}' 
    #course_code.short_description='complete'
    #fields=(('first_name','last_name'),('matricule','course'), 'gender', 'date_of_birth')
    """fieldsets = (
        ('SCHOOL INFO', {
            'fields': (
                ('first_name','last_name'),
                ('matricule','course'),
            ),
        }),


        ('PERSON INFO',{
             'classes':('collapse','wide',),
             'fields':(
                ('gender','date_of_birth')
             ),
             'description':'This a new group'
        }),

    )"""
    #exclude=('last_name','date_of_birth')
    


admin.site.register(CustomUser)
admin.site.register(Student, StudentAdmin)
