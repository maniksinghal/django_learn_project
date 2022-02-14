from django.db import models

class Blog(models.Model):
    #Google Django model field reference for more information
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    #Stringified name of the model's object
    #Viewed in admin page
    def __str__(self):
        return self.title
