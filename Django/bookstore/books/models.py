from django.db import models

class author(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=80)
    created = models.DateTimeField('date created')
class book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=80)
    created = models.DateTimeField('date created')
    author = models.ForeignKey(author, on_delete= models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True)
