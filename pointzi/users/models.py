from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=120, null=False,
        verbose_name="First Name")
    email=models.EmailField(max_length=120, null=False, 
        verbose_name="Email")
    country=models.CharField(max_length=30, null=False, 
        verbose_name="Country")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Created")
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-created"]  # <=====
        
    def __str__(self):
        return self.email  # <=====
        
