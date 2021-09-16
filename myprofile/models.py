from django.db import models


# Create your models here.

STATUS = (
    (0, "Deactive"),
    (1, "Active")
)

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, default="")
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.name
        
class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/project", default="", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    project_info = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    technology = models.CharField(max_length=200, blank=True, null=True)
    link_title_name = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title
        
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True, default="")
    msg = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
