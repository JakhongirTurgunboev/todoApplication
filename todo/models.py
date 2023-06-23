from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    task_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
