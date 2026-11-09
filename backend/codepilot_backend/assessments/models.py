from django.db import models

# Create your models here.

class Assessment(models.Model):

    title = models.CharField(max_length=200)

    description=models.TextField()

    instructions=models.CharField(max_length=200)

    duration=models.IntegerField()

    STATUS_CHOICES = [
    ('pending','Pending'),
    ('in_progress','In Progress'),
    ('completed','Completed'),
    ('cancelled','Cancelled')
]
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default="in_progress")

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assessments"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

