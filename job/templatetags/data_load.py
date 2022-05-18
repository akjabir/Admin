from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from job import models
register = template.Library()

@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep

@register.filter(name='menu')
def menu_list(obj):
    all_job_data  = models.all_job.objects.filter(status = True).order_by('catagory','title')
    return all_job_data
