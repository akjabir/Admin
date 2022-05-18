import os
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class category(models.Model):
    cate_name = models.CharField(max_length = 200)
    ordering = models.IntegerField(default= 0 )
    meta_description = models.TextField(blank = True)
    meta_keywords    = models.TextField(blank = True)
    meta_title       = models.TextField(blank = True)
    status     		 = models.BooleanField(default=True)

    def __str__(self):

	    return self.cate_name

    class Meta:
	    verbose_name ='category'
	    verbose_name_plural ='catagories'  
  
class all_job(models.Model):
	catagory 		   = models.ForeignKey(category , on_delete = models.CASCADE)
	title              = models.CharField(max_length = 200)
	title_url          = models.CharField(max_length = 200, unique= True, blank= True, null = True)
	post_date_time	   = models.DateField(auto_now_add=False,blank=True)
	images             = models.FileField(upload_to="service_images/")
	image_alt_tag      = models.CharField(max_length = 200, blank = True)
	details            = RichTextField(blank = True)
	meta_description   = models.TextField(blank = True)
	meta_keywords      = models.TextField(blank = True)
	meta_title         = models.TextField(blank = True)
	ordering 		   = models.IntegerField(default = 0)
	views   		   = models.IntegerField(default = 1)
	status     		   = models.BooleanField(default=True)
	


	def __str__(self):
		return self.title

	class Meta:
		verbose_name ='all_job'
		verbose_name_plural ='all_jobs'


class SeoContent(models.Model):
	index_meta_title        = models.TextField(blank = True)	
	index_meta_description  = models.TextField(blank=True)
	index_meta_keywords     = models.TextField(blank = True)
	status             =models.BooleanField(default=True)

	def __str__(self):
		return self.index_meta_title   

	class Meta:
		verbose_name = 'Seo Content'
		verbose_name_plural = 'Seo Contentes'

class govcategory(models.Model):
	govcat_details 	          = RichTextField(blank = True)
	meta_description   		  = models.TextField(blank = True)
	meta_keywords      		  = models.TextField(blank = True)
	meta_title			      = models.TextField(blank = True)

	def __str__(self):
		return self.govcat_details
	
	class Meta:
		verbose_name = 'govcategory'
		verbose_name_plural = 'govcategories'	
