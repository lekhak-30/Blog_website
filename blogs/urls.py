from django.urls import path
from . import views
app_name = 'blogs'
urlpatterns = [
    path('category/<int:category_id>/', views.category_view, name='category_detail'),
    path('blogs/',views.Blogs, name='blogs')
]
