from django.shortcuts import render
from blogs.models import Category,Blogs
def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_feacherd=True)
    context = {
        'categories':categories,
        'featured_post':featured_post
    }
    return render(request, 'home.html',context)

