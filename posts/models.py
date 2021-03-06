from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.TextField(
        'Body', blank=False, null=False, max_length=140, db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )

    likes = models.PositiveIntegerField(
        'like', default=0, blank=True, db_index=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )