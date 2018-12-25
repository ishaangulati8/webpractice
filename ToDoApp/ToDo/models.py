from django.db import models


# Create your models here.
class toDo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return 'Text: ' + self.text + ' Completed: ' + str(self.complete)
