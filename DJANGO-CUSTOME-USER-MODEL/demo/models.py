from django.db import models

# Create your models here.
from django.db import models

class AssertModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'AssertModel'
        managed = True
        verbose_name = 'Assert'
        verbose_name_plural = 'Assert'

    def __str__(self):
        return self.name

class Person(models.Model):
    full_name = models.CharField(max_length=100)

    # MANY TO MANY relationship
    asserts = models.ManyToManyField(
        AssertModel,
        related_name="persons"   # parent → child access
    )

    class Meta:
        db_table = 'Person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.full_name
