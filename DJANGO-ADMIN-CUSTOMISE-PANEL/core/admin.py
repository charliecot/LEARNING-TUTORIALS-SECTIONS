from django.contrib import admin
from .models import Course, Lesson

# Register your models here.
admin.site.site_header="Course Management Admin"
admin.site.site_title="Course Admin"

# it is used to create a custom admin interface for the Lesson model, which is displayed as an inline form within the Course admin interface. This allows users to add and edit lessons directly from the course detail page in the admin panel.
class LessonInline(admin.TabularInline):
    model = Lesson
    max_num = 3
    extra = 1
    exclude = ("video_url",)
    can_delete = False
    verbose_name_plural="Lessons-Inline"
    classes = ("collapse",)





#this help us to create a custom admin interface for the Lesson model, which is displayed as an inline form within the Course admin interface. This allows users to add and edit lessons directly from the course detail page in the admin panel.
""" class LessonInline(admin.StackedInline):
    model = Lesson
     """



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # it helps to display the fields in the list view of the admin panel
    list_display = ("title", "author", "status", "publish_date", "price", "conbine_title_and_author","capital_title")

    list_editable = ("status", "price")  # it helps to make the fields editable in the list view of the admin panel

    # it helpp to exclude or remove the fields from the list view of the admin panel
    #exclude = ("title","price")

    list_filter=('title', 'publish_date')  # it helps to filter the fields in the list view of the admin panel

    #conver a fields to a link to the change view of the object in the list view of the admin panel
    list_display_links = ("title","publish_date")
    #search_fields=("title__startswith","price__gte")  # it helps to search the fields in the list view of the admin panel
    search_fields=("title",)  # it helps to search the fields in the list view of the admin panel
   
    #ordering = ("title",)  # it helps to order the fields in the list view of the admin panel
    #we cannot use fields and fieldsets together, so we will comment out the fields attribute
    #fields = (("title","price"), "author",  "publish_date", "status",)



    # this use of fieldsets allows us to group fields together and also add a description to the group
    fieldsets=(
        ('Basic Information',{
            'fields': (("title",  "publish_date"),  "price")
        }),
        ('Extra Info',{
            'classes':('collapse','wide'),
            'fields': ("author", "status"),
            'description': "Additional information about the course"
        }))
    list_per_page = 5 # it helps to set the number of items to display per page in the list view of the admin panel
    readonly_fields = ("status",)  # it helps to make the fields read-only in the list view of the admin panel

    inlines = [LessonInline]  # it helps to display the related objects in the list view of the admin panel



    def get_ordering(self, request):
            if request.user.is_superuser:
                return ("title", "publish_date")
            else:
             return ("-price",)  # it helps to order the fields in the list view of the admin panel
    

    #helps to add custom actions to the list view of the admin panel
    @admin.display(boolean=True, description="Name and Price")
    def conbine_title_and_author(self, obj):
        return True  #f"{obj.title} by {obj.price}"
    
   #conbine_title_and_author.short_description = "Title and Author"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course" )
    #list_editable = ("position",)
    list_filter = ("course__status",)
    search_fields = ("course__price__gte",)
    #autocomplete_fields = ("course",)
    raw_id_fields = ("course",)





""" admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin) """