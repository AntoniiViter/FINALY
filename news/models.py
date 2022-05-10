from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datearchived = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True)
    newscreator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s) [%s]" % (self.title, self.pk, self.newscreator)


class Comments(models.Model):
    commentcreator = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, db_constraint=False)
    info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s [%s] (%s)" % (self.commentcreator.title, self.info, self.pk)
