from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return self.name
