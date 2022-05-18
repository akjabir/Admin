from django.contrib import admin
from . import models

class categoryAdmin(admin.ModelAdmin):
    list_display     = ['cate_name', 'ordering', 'status']
    search_fields    = ['title']
    list_filter      = ['status']
    
class all_jobAdmin(admin.ModelAdmin):
    list_display     = ['catagory','title','title_url','views','ordering', 'status']
    search_fields    = ['title']
    list_filter      = ['status']


class SeoContentAdmin(admin.ModelAdmin):
    list_display     = ['index_meta_title', 'status']
    list_filter      = ['status']

class govcategoryAdmin(admin.ModelAdmin):
    list_display     = ['govcat_details']

admin.site.register(models.category, categoryAdmin)
admin.site.register(models.all_job, all_jobAdmin)
admin.site.register(models.SeoContent, SeoContentAdmin)
admin.site.register(models.govcategory, govcategoryAdmin)
