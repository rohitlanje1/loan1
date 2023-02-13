from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    ROLE_CHOICES = [('Customer', 'Customer'), ('Loan_Representative', 'Loan_Representative'), ('Operational_Head', 'Operational_Head'), ('Loan_Sanction_Officer', 'Loan_Sanction_Officer'), ('Admin', 'Admin')]
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    signature = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    role = models.CharField(max_length=50, default='Customer', choices=ROLE_CHOICES)
    # loan_representative_status=models.CharField(max_length=10)
    # operational_head_status=models.CharField(max_length=10)
    
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile','email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
        
    def __str__(self):
        return f'{self.email}'

class Defaulter(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Defaulters')
    default_amount = models.FloatField(default=0, blank=True)
    pending_since_date = models.DateField(default="2000-12-12", blank=True)

    def __str__(self):
       	return f"{self.user.email}"
    


