from django.db import models
from django.utils import timezone
from django.urls import reverse

from uuid import uuid4

def upload_directory(instance, filename):
    d = timezone.now()
    i = str(uuid4())
    return 'media/'+'{0}/{1}.{2}'.format(
        d.strftime('%Y/%m/%d/%H/%M'),
        i,
        filename.split('.')[-1])


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    img_link = models.CharField(max_length=200,blank=True, null=True)
    audio_file = models.FileField(blank=True, null=True, upload_to=upload_directory)
    image_file = models.FileField(blank=True, null=True, upload_to=upload_directory)
    category        = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    img_label       = models.TextField(blank=True, null=True, help_text='Separate each item by comma') 
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    is_digital      = models.BooleanField(default=False)   
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    alert = models.CharField(max_length=200,blank=True, null=True)   
    tags = models.TextField(blank=True, null=True, help_text='Separate each item by comma') 
    content = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=1024,blank=True, null=True)
    slug = models.SlugField(unique = True, db_index=True, null=True)
    pic = models.URLField(max_length = 400)
    address = models.CharField(max_length = 150)
    lide = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)



    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    def get_category(self):
        return self.category.split(",")

    def get_img_label(self):
        return self.img_label.split(",")
