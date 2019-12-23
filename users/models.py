from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class UserTable(AbstractUser):
    birthday = models.DateField(("Date"), default=date.today)
    student_no = models.IntegerField(default = 0,validators=[MinValueValidator(10000), MaxValueValidator(999999)],unique=True)
    tc_no = models.IntegerField(default = 0,validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)],unique=True)
    department = models.CharField(max_length = 100)
    image =models.ImageField(upload_to='images/', null=True, blank=True)
    telephone = models.CharField(max_length = 20, blank = True, null = True)

    USERNAME_FIELD = 'student_no'
    
    def __str__(self):
        return self.username
    class Meta:
        unique_together = ('username', 'student_no','tc_no')
    
