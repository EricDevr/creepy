from django.db import models

# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/images")
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    def __str__(self):
        return self.title