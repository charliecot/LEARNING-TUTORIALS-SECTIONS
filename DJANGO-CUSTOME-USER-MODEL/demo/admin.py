from django.contrib import admin
from .models import AssertModel,Person
# Register your models here.

@admin.register(AssertModel)
class AssertAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)
    search_fields=('name__startswith',)
    list_per_page=3


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('full_name','get_list')
    list_filter=('full_name',)
    search_fields=('full_name__startswith',)
    list_per_page=3
    @admin.display(description='Assets_list')
    def get_list(self,obj):
        result = ",".join(a.name for a in obj.asserts.all())
        return result
    list_display_links=('get_list',)
    list_editable= ('full_name',)
    raw_id_fields=('asserts',)



