from django.db import models
from django.contrib import admin

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class CustomerUserManger(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('user must have an email address')
        if not username:
            raise ValueError('user must have a username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,first_name,last_name,username,email,password=None):
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    RESTAURANT=1
    CUSTOMER=2
    ROLES_CHOICES=(
        (RESTAURANT,'restaurant'),
        (CUSTOMER,'customer')
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    role=models.PositiveSmallIntegerField(choices=ROLES_CHOICES,blank=True,null=True)

    #required fields
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    
    # authentication field in this case email will be use to authenticate

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    objects=CustomerUserManger()

    def __str__(self):
        return self.email
    
    #check if the user has permission

    def has_perm(self, perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_lable):
        return True

    

 
from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    @admin.display(description='new_data')
    def capitalised_column(self):
        return '{}'.format(self.first_name).upper()
    





class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ('car', 'Car'),
        ('bike', 'Motorbike'),
        ('truck', 'Truck'),
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    color = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
class VehicleRegistration(models.Model):
    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='registration'
    )

    plate_number = models.CharField(max_length=20, unique=True)
    engine_number = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.plate_number
   
    

