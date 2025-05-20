from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('Sales', 'Sales'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=20000)  # e.g., 75000.00
    experience = models.PositiveIntegerField(help_text="Years of experience required", default=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='IT')  # Default added here
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# Create your models here.
