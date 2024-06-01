from django.contrib import admin
from .models import *

# Register your models here.

class TagTublerInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    list_display = ['title', 'author', 'date', 'status', 'section', 'main_post', 'category']
    list_editable = ['status', 'section', 'main_post', 'category']
    search_fields = ['title', 'author', 'section']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)



class PoliticalAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'author', 'date', 'status', 'section', 'main_post', 'category']
    list_editable = ['status', 'section', 'main_post', 'category']
    search_fields = ['title', 'author', 'section']

admin.site.register(Categorys)
admin.site.register(Political, PoliticalAdmin)


class FinanceAdmin(admin.ModelAdmin):
 
    list_display = ['title', 'author', 'date', 'status', 'section', 'main_post', 'category']
    list_editable = ['status', 'section', 'main_post', 'category']
    search_fields = ['title', 'author', 'section']

admin.site.register(Categoryfinance)
admin.site.register(finance, FinanceAdmin)
