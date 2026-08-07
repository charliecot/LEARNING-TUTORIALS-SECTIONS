from django.contrib import admin

from .models import Person, Course, Grade

# ===========================
# DATABASE / ORM
# ===========================
from django.db.models import Avg

# ===========================
# HTML UTILITIES
# ===========================
from django.utils.html import format_html

# ===========================
# URLS
# ===========================
from django.urls import reverse
from django.utils.http import urlencode

# ===========================
# FORMS
# ===========================
from django import forms

# ===========================
# Register your models here.
# ===========================


class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    # Custom Validation
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]

        if first_name == "Spike":
            raise forms.ValidationError("No Vampire!!!")

        return first_name


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    # ---------------------------------------------------------
    # LIST PAGE
    # ---------------------------------------------------------
    list_display = (
        "first_name",
        "last_name",
        "email",
        "date_of_birth",
        "show_average",
    )

    list_display_links = (
        "first_name",
        "last_name",
    )

    ordering = (
        "-last_name",
        "first_name",
    )

    # Search Box
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

    # Filters
    list_filter = (
        "date_of_birth",
    )

    # Read only fields
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Uncomment if you want manual field ordering
    # fields = (
    #     "first_name",
    #     "last_name",
    #     "email",
    #     "date_of_birth",
    # )

    # IMPORTANT
    # It is form, NOT forms
    form = PersonAdminForm

    @admin.display(description="Average Grade", ordering="grade__grade")
    def show_average(self, obj):

        avg = obj.grade_set.aggregate(avg=Avg("grade"))["avg"]

        if avg is None:
            return format_html(
                "<span style='color:gray;'>No grades</span>"
            )

        color = "green" if avg >= 50 else "red"

        return format_html(
            "<span style='color:{}; font-weight:bold;'>{}</span>",
            color,
            avg
        )

    """
    @admin.display(description='Average Length of Last Name')
    def show_average(self,obj):

        result = Grade.objects.filter(person=obj).aggregate(Avg('grade'))

        text = 'end'

        avg = int(result['grade__avg'])

        color = 'green'

        if avg < 90 and avg > 60:
            color = 'blue'

        elif avg <= 60:
            color = 'red'

        return format_html(
            "<span style='color:{}; text-align:{};'>{}</span>",
            color,
            text,
            avg
        )
    """

    # Change labels dynamically
    def get_form(self, request, obj=None, change=False, **kwargs):

        form = super().get_form(
            request,
            obj,
            change=change,
            **kwargs,
        )

        form.base_fields[
            "first_name"
        ].label = "First Name (Human Only!)"

        return form


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    # ---------------------------------------------------------
    # LIST PAGE
    # ---------------------------------------------------------

    list_display = (
        "name",
        "start_date",
        "end_date",
        "year",
        "student_count",
        "view_students_link",
    )

    list_display_links = (
        "name",
    )

    ordering = (
        "name",
    )

    list_filter = (
        "year",
    )

    search_fields = (
        "name",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    @admin.display(description="Students")
    def student_count(self, obj):
        return obj.students.count()

    @admin.display(description="View Students")
    def view_students_link(self, obj):

        number_of_students = obj.students.count()

        # Filter students enrolled in this course
        url = (
            reverse(
                "admin:custom_admin_app_person_changelist"
            )
            + "?"
            + urlencode(
                {
                    # Adjust this lookup if needed
                    "course__id": obj.id
                }
            )
        )

        return format_html(
            "<a href='{}'>View ({})</a>",
            url,
            number_of_students,
        )


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "person",
        "grade",
    )

    list_display_links = (
        "course",
        "person",
    )

    ordering = (
        "course",
        "person",
    )

    search_fields = (
        "course__name",
        "person__first_name",
        "person__last_name",
    )

    list_filter = (
        "course",
    )