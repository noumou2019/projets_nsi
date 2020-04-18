from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Exercices(models.Model):
    """
    model pour gerer les exercices 
    """
    name = models.CharField(max_length=150)
    ennoncer = RichTextField(blank=True)
    datecreation = models.DateField(auto_now_add=True)
    publier_exos = models.IntegerField(choices=STATUS, default=0)
    exercice_post = models.ForeignKey(Post, on_delete=models.CASCADE)


# class Devoirs(models.Model):

#     nomprenom = models.CharField(max_length=150)
#     classes = models.CharField(max_length=150)
#    ## fichier = models.FileField(upload_to ="../devoirs")
#     publier_devoir = models.IntegerField(choices=STATUS, default=0)
#     devoir_post = models.ForeignKey(Post, on_delete=models.CASCADE)

