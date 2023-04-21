from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')
    image = models.ImageField(upload_to='images',null=True, blank=True)
    content = RichTextUploadingField()
    visible = models.BooleanField(default=1)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title