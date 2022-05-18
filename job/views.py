from django.shortcuts import render
from .import models
from django.db.models import F,Q
from django.http import JsonResponse
from django.core.paginator import Paginator


def index(request):
    seo_contain   = models.SeoContent.objects.filter(status = True).first()
    letest  = models.all_job.objects.filter(status = True).order_by('-id')
    popular_post    = models.all_job.objects.filter(status = True).order_by("views")
    all_job_data  = models.all_job.objects.filter(status = True).order_by('catagory')
    context ={
        'seo_contain'  : seo_contain,
        'letest'  : letest,
        'popular_post': popular_post,
        'all_job_data' : all_job_data,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.all_job.objects.filter(title_url__icontains = product)
        return render(request, 'job/search_result.html',{'product_list' : product_list, 'product' : product})

    return render(request, 'job/index.html',context)

def all_job(request, nam):
    name = nam.replace('-', ' ') 
    request.session["category_name"] = name
    category_data   = models.all_job.objects.filter(status = True, catagory_id__cate_name = name)
    seo_contain     = models.all_job.objects.filter(status = True, catagory_id__cate_name = name).first()

    paginator = Paginator(category_data, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    category_data = paginator.get_page(page_number)
    context ={
        'category_data' : category_data,
        'seo_contain' : seo_contain,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.all_job.objects.filter(title_url__icontains = product)
        
    return render(request,'job/cate_data.html', context)


def single_post(request, name, nam):
    name1 = nam.replace('-', ' ') 
    single_data     = models.all_job.objects.filter( title_url = name1 ).first()
    if single_data :
        single_data     = models.all_job.objects.filter( title_url = name1 ).first()
    else:
        single_data = 0
        
    rel_post        = models.all_job.objects.filter(status = True, catagory_id = single_data.catagory_id).exclude(title_url = name1).order_by("-id")
    popular_post    = models.all_job.objects.filter(status = True,catagory_id = single_data.catagory_id).exclude(title_url = name1).order_by("views")
    models.all_job.objects.filter(title_url = name1 ).update(views = F('views') + 1)

    context ={
        'single_data':single_data,
        'rel_post': rel_post,
        'popular_post': popular_post,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.Service.objects.filter(title_url__icontains = product)
        return render(request, 'job/search_result.html',{'product_list' : product_list, 'product' : product})
    
    return render(request,'job/single_page.html', context)

def govcategory(request):
    govcategory = models.govcategory.objects.first()
    context = {
        'govcategory'  : govcategory,
    }
    return render(request, 'job/govcategory.html', context)

