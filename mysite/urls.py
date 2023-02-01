"""mysite URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from .views import index, about_us, contact_us, blog_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),

    path('about-us', about_us, name="about-us"),
    path('contact-us', contact_us, name="contact-us"),
    
    path('blog/', include('blog.urls', namespace='blog')),
    path('blog-list-view', blog_list_view, name='blog-list-view')
   
    
]
