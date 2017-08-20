from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='description')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    img = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    IMG_TYPES = (
        ('WIP', 'Work in Progress'),
        ('STD', 'Finished Work'), #STD -> Standard Arts/Work
        ('PRF', 'Profile Image'),
    )
    img_type = models.CharField(default='Finished Work', max_length=3, choices=IMG_TYPES)
    # edited_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-upload_date"]
