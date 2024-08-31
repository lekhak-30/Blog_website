from django.contrib import admin
from .models import Blogs,Category
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category' , 'author','blog_image', 'status','is_feacherd','created_at','update_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)
    search_fields = ('id', 'title', 'category__category_name', 'status', 'content')
    list_editable = ('is_feacherd',)
    actions = ['delete_selected']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name' , 'created_at' , 'update_at')
    
    actions = ['delete_selected']
    

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
