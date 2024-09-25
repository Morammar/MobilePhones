from django.db import models


# Create your models here.
class BlogPost(models.Model):
    product = models.CharField(max_length=100)
    price = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title