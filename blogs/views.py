from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'  # Path to your template
    context_object_name = 'categories' 