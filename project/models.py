from django.db import models
from datetime import date
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.



class Task(models.Model):
    deadline = models.DateField(null=True,blank=True)
    title = models.CharField(max_length=50,blank=False)
    desc = RichTextUploadingField (blank=True,null=True)

    remarks = RichTextUploadingField(blank=True,null=True)


    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_requests_created',on_delete=models.CASCADE,blank=False,null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=False,null=True)
    in_review = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    


    def get_status(self):
        if date.today() > self.deadline:
            return 1
        
        elif self.in_review:
            return 2

        return 0

    def set_review(self):
        self.in_review = True
        self.save()


    