from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    popular = Post.objects.filter(section = 'Popular').order_by('-id')[0:4]
    recent = Post.objects.filter(section = 'Recent').order_by('-id')[0:4]
    main = Post.objects.filter(section = 'main_post').order_by('-id')[0:1]
  
    editor = Post.objects.filter(section = 'Editor_pick').order_by('-id')
    tranding = Post.objects.filter(section = 'Tranding').order_by('-id')
    Inspiration = Post.objects.filter(section = 'Inspiration').order_by('-id')[0:6]
    Latest_post = Post.objects.filter(section = 'Latest_post').order_by('-id')[0:4]
    catogary =Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'popular':popular,
        'recent':recent,
        'editor':editor,
        'main':main,
        'tranding': tranding,
        'Inspiration':Inspiration,
        'Latest_post':Latest_post,
        'catogary':catogary,
        'tags':tags
        
        
    }
    return render(request,"index.html",context)

def political(request):
    popular = Political.objects.filter(section = 'Popular').order_by('-id')[0:4]
    recent = Political.objects.filter(section = 'Recent').order_by('-id')[0:4]
    main = Political.objects.filter(section = 'main_post').order_by('-id')[0:1]
  
    editor = Political.objects.filter(section = 'Editor_pick').order_by('-id')
    tranding = Political.objects.filter(section = 'Tranding').order_by('-id')
    Inspiration = Political.objects.filter(section = 'Inspiration').order_by('-id')[0:6]
    Latest_post = Political.objects.filter(section = 'Latest_post').order_by('-id')[0:4]
    catogary =Categorys.objects.all()
    
    context = {
        'popular':popular,
        'recent':recent,
        'editor':editor,
        'main':main,
        'tranding': tranding,
        'Inspiration':Inspiration,
        'Latest_post':Latest_post,
        'catogary':catogary,
        
        
        
    }
    return render(request,"political.html",context)



def Finance(request):
    popular = finance.objects.filter(section = 'Popular').order_by('-id')[0:4]
    recent = finance.objects.filter(section = 'Recent').order_by('-id')[0:4]
    main = finance.objects.filter(section = 'main_post').order_by('-id')[0:1]
  
    editor = finance.objects.filter(section = 'Editor_pick').order_by('-id')
    tranding = finance.objects.filter(section = 'Tranding').order_by('-id')
    Inspiration = finance.objects.filter(section = 'Inspiration').order_by('-id')[0:6]
    Latest_post = finance.objects.filter(section = 'Latest_post').order_by('-id')[0:4]
    catogary =Categoryfinance.objects.all()
  
    context = {
        'popular':popular,
        'recent':recent,
        'editor':editor,
        'main':main,
        'tranding': tranding,
        'Inspiration':Inspiration,
        'Latest_post':Latest_post,
        'catogary':catogary,
        
        
        
    }
    return render(request,"finance.html",context)



def About(request):
    popular = Post.objects.filter(section = 'Popular').order_by('-id')[0:4]
    recent = Post.objects.filter(section = 'Recent').order_by('-id')[0:4]
    main = Post.objects.filter(section = 'main_post').order_by('-id')[0:1]
  
    editor = Post.objects.filter(section = 'Editor_pick').order_by('-id')
    tranding = Post.objects.filter(section = 'Tranding').order_by('-id')
    Inspiration = Post.objects.filter(section = 'Inspiration').order_by('-id')[0:6]
    Latest_post = Post.objects.filter(section = 'Latest_post').order_by('-id')[0:4]
    catogary =Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'popular':popular,
        'recent':recent,
        'editor':editor,
        'main':main,
        'tranding': tranding,
        'Inspiration':Inspiration,
        'Latest_post':Latest_post,
        'catogary':catogary,
        'tags':tags
        
        
    }
    return render(request,"about.html",context)

def contact(request):
    return render(request,"contact.html")