from users.models import User
from django.db import models

# Create your models here.

class Book(models.Model):
    book_title=models.CharField(max_length=120, null=False, 
        verbose_name="Book Title")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="user_id", 
        verbose_name="User ID")
    book_author=models.CharField(max_length=120, null=False,
        verbose_name="Book Author")
    ISBN=models.CharField(max_length=13, null=False, 
        verbose_name="ISBN")
    date_added = models.DateTimeField(auto_now_add=True,
        verbose_name="Date Added")
    
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ["-date_added"]  # <=====
        
    def __str__(self):
        return self.book_title  # <=====
