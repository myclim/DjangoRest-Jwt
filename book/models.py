from django.db import models
from user.models import User

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(default='', verbose_name="Content")
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name="users",
        verbose_name="User"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    class Meta:
        db_table = "book"
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return f"{self.user.username} - {self.title}"