from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in weeks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
