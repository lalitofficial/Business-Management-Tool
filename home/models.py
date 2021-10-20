from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


class OTree(models.Model):

    node = models.OneToOneField(Group,on_delete=models.CASCADE,primary_key=True,related_name="node")
    parent  = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="parent")


    def __str__(self):
        return self.node.name
