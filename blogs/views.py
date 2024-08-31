from django.shortcuts import render
from .models import Blogs,Category
# Create your views here.
from django.views.generic import ListView
from .models import Category

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = BlogPost.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'posts': posts})

