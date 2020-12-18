from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def validate_time(date):
    if date < timezone.now():
        raise ValidationError("Date can't be in the past")

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=2, null=False)
    zip_code = models.CharField(max_length=12, null=False)
    city = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    admin = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Quotes(models.Model):
    date_submitted = models.DateTimeField(default=timezone.now(), editable=False)
    start_date_requested = models.DateTimeField(null=False, validators=[validate_time])
    end_date_requested = models.DateTimeField(null=False, validators=[validate_time])
    quoted_price = models.CharField(max_length=50)
    final_cost = models.CharField(max_length=50)
    completed = models.BooleanField(null=False, default=False)
    accepted = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} submitted on {self.start_date_requested}"