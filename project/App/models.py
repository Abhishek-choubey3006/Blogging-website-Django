from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = {
        ('0','DRAFT'),
        ('1','PUBLISH'),
    }
    SECTION = {

        
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editor_pick','Editor_pick'),
        ('Tranding','Tranding'),
        ('Inspiration','Inspiration'),
        ('Latest_post','Latest_post'),
        ('main_post','main_post'),
    }

    Feature_image = models.ImageField(upload_to='media',blank=False,null=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content =RichTextField()
    slug = models.SlugField(max_length=400,null=True,blank=True,unique=True)
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)
    main_post = models.BooleanField(default=False)
    author_image = models.ImageField(upload_to='media',blank=True,null=True)

    def __str__(self):
        return self.title
    
def create_Slug(instance,newslug = None):
    slug = slugify(instance.title)
    if newslug is not None:
        slug = newslug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists
    if exists:
        newslug = "%s=%s" %(slug,qs.first().id)
        return create_Slug(instance,newslug=newslug)
    return slug

def pre_save_post(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_Slug(instance)
    pre_save.connect(pre_save_post,Post)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Political(models.Model):
    STATUS = {
        ('0','DRAFT'),
        ('1','PUBLISH'),
    }
    SECTION = {

        
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editor_pick','Editor_pick'),
        ('Tranding','Tranding'),
        ('Inspiration','Inspiration'),
        ('Latest_post','Latest_post'),
        ('main_post','main_post'),
    }

    Feature_image = models.ImageField(upload_to='media/Political',blank=False,null=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content =RichTextField()
    slug = models.SlugField(max_length=400,null=True,blank=True,unique=True)
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)
    main_post = models.BooleanField(default=False)
    author_image = models.ImageField(upload_to='media',blank=True,null=True)

    def __str__(self):
        return self.title
def create_Slug(instance,newslug = None):
    slug = slugify(instance.title)
    if newslug is not None:
        slug = newslug
    qs = Political.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists
    if exists:
        newslug = "%s=%s" %(slug,qs.first().id)
        return create_Slug(instance,newslug=newslug)
    return slug

def pre_save_post(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_Slug(instance)
    pre_save.connect(pre_save_post,Political)

class Categorys(models.Model):
    name = models.CharField(max_length=200)

# class Tags(models.Model):
#     name = models.CharField(max_length=200)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    


class finance(models.Model):
    STATUS = {
        ('0','DRAFT'),
        ('1','PUBLISH'),
    }
    SECTION = {

        
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editor_pick','Editor_pick'),
        ('Tranding','Tranding'),
        ('Inspiration','Inspiration'),
        ('Latest_post','Latest_post'),
        ('main_post','main_post'),
    }

    Feature_image = models.ImageField(upload_to='media/Finance',blank=False,null=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content =RichTextField()
    slug = models.SlugField(max_length=400,null=True,blank=True,unique=True)
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)
    main_post = models.BooleanField(default=False)
    author_image = models.ImageField(upload_to='media',blank=True,null=True)

    def __str__(self):
        return self.title
def create_Slug(instance,newslug = None):
    slug = slugify(instance.title)
    if newslug is not None:
        slug = newslug
    qs = finance.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists
    if exists:
        newslug = "%s=%s" %(slug,qs.first().id)
        return create_Slug(instance,newslug=newslug)
    return slug

def pre_save_post(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_Slug(instance)
    pre_save.connect(pre_save_post,finance)

class Categoryfinance(models.Model):
    name = models.CharField(max_length=200)

# class Tagsfinance(models.Model):
#     name = models.CharField(max_length=200)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
