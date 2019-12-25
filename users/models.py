from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class UserTable(AbstractUser):
    birthday = models.DateField(("Date"), default=date.today)
    student_no = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)],unique=True)
    tc_no = models.IntegerField(default=10000000000,validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)])
    department = models.CharField(max_length = 100)
    image =models.ImageField(upload_to='images/', null=True, blank=True)
    telephone = models.CharField(max_length = 20, blank = True, null = True)
    graduate_year=models.IntegerField(default=2020,validators=[MinValueValidator(1955), MaxValueValidator(2300)])
    foreign_languages=models.CharField(max_length = 200)
    certificates=models.CharField(max_length = 200)
    USERNAME_FIELD = 'student_no'
    REQUIRED_FIELDS = ['username','email']
    def __str__(self):
        return self.username
    class Meta:
        unique_together = ('username', 'student_no','tc_no')

# TO DO Message
# Working position
# Company class
