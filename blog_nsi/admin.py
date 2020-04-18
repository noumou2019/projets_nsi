from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('name', 'datecreation', 'publier_exos','exercice_post')
    list_filter = ("name",)
    search_fields = ['name', 'ennoncer']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Exercices, ExerciceAdmin)