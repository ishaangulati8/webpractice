from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Name : {}, Id : {}'.format(self.name,self.id)