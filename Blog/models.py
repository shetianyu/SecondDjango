from django.db import models
from django.contrib import  admin
from Blog.postxml import SendRtx
from django import forms
from django.forms import ModelForm


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body  = models.TextField()
    timestamp = models.DateTimeField()
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

