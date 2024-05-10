from django.db import models
from django.contrib.auth.models import AbstractBaseUser,Group
from django.db import models
from .manager import UserManager
# Create your models here.



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=60,blank=False,null=False)
    phone=models.CharField(max_length=13,blank=False,null=False,unique=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.TextField()
    ROLE_CHOICES = (
        
        ('admin', 'Admin'),
        ('customer','customer'),
        ('driver','driver')
        
    )
    user_type = models.CharField(max_length=20,default='customer', choices=ROLE_CHOICES)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.phone}{self.full_name}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    


class GarbageBin(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    assigned = models.BooleanField(default=False)

    def __str__ (self):
        return self.name
    

class UserGarbageBin(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ManyToManyField(GarbageBin)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    


class CollectionRequest(models.Model):
    garbage = models.ForeignKey(UserGarbageBin,on_delete=models.DO_NOTHING)
    COLLECTION_CHOICES = (
        
        ('filled', 'filled'),
        ('half','half'),
        
        
    )
    status = models.CharField(max_length=20,default="filled",choices=COLLECTION_CHOICES)
    REQUEST_CHOICES = (
        
        ('pending', 'pending'),
        ('approved','approved')
        
        
    )
    
    request_status = models.CharField(max_length=20,default="pending",choices=REQUEST_CHOICES)
    driver = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


class CollectionStatus(models.Model):
    collectonrequest = models.ForeignKey(CollectionRequest,on_delete=models.DO_NOTHING)
    STATUS_CHOICES = (
        
        ('collected', 'collected'),
        ('not_collected','not collected'),
        ('on_the_way','on the way')


        
        
    )
    
    request_status = models.CharField(max_length=20,default="not_collected",choices=STATUS_CHOICES)



class Complaint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    issue = models.TextField()





    


