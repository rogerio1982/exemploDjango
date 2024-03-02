from django.db import models
# teste github !!!

class produto(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

