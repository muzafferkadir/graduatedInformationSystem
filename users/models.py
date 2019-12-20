from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class UserTable(AbstractUser):
    birthday = models.DateField(("Date"), default=date.today)
    student_no = models.IntegerField(default = 0,validators=[MinValueValidator(10000), MaxValueValidator(999999)])
    tc_no = models.IntegerField(default = 0,validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)])
    department = models.CharField(max_length = 100)
    #image =models.ImageField(upload_to='images/')
    telephone = models.CharField(max_length = 20, blank = True, null = True)

    def __str__(self):
        return self.username