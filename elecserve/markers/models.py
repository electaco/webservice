from django.db import models
from django.contrib.auth.models import User

class AnetUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anetname = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("Category", blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
class MarkerPack(models.Model):
    data = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pack_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    added = models.DateField(auto_now_add=True)
    updated = models.DateField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def query_result(self):
        return {"title": self.title, "id": self.id, "category": self.category.name, "uploader": self.added_by.username}

    def __str__(self):
        return self.title