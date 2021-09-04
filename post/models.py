from django.db import models

# Create your models here.
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.IntegerField()
    user = models.CharField(max_length=50)
    comment = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user