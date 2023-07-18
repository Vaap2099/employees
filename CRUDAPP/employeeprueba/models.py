from django.db import models
 
class Employee(models.Model):
    Id = models.CharField(max_length=5)
    Name = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    HomeTel = models.CharField(max_length=9)
    MobileTel = models.CharField(max_length=9)
    State = models.CharField(max_length=10)
    BusinessId = models.CharField(max_length=5)
    DepartmentId = models.CharField (max_length=5)
    UnitId = models.CharField (max_length=5)

    class Meta:
        db_table = "employee"
        ordering = ['-created_at']