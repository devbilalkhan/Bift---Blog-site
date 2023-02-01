from django.urls import path
from .import views


'''application namespace variable
   To organize URLs by app name
'''
app_name = 'blog'

urlpatterns = [
    
    path('posts/', views.post_list, name='post_list'),    
    path('posts/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share')

]
