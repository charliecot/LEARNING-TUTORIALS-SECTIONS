from django.db import models
from django.contrib import admin


class Course(models.Model):
    class CourseStatus(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=CourseStatus.choices,
        default=CourseStatus.DRAFT,
    )
    
    def __str__(self):
        return self.title
    
    @admin.display(description="Capitalized Title")
    def capital_title(self):
        return self.title.upper()    


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    position = models.PositiveIntegerField()
    video_url = models.URLField()

    """ class Meta:
        ordering = ["position"]
        unique_together = ("course", "position")

    def __str__(self):
        return f"{self.position}. {self.title}" """
# Create your models here.
