from django.db import models

class members(models.Model):
    FullName = models.CharField(max_length=200)
    Gender = models.CharField(max_length=6)
    SponNo = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=15)
    State = models.CharField(max_length=50)
    LocalGov = models.CharField(max_length=100)
    Status = models.CharField(max_length=15)
    

    def __str__(self):
        return self.FullName