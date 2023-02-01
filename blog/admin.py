from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
    Customize the admin post display panels
    '''
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', "created", "publish"]
    search_fields = ["title", "body"]
    prepopulated_fields = {'slug' : ("title",)}
    date_hierarchy = 'publish'
    # creates sort order
    ordering = ["status", "publish"] 
    raw_id_fields = ["author"]