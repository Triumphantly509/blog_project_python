from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    search_fields = ('title',)  
    list_filter = ('date_published',) 
      
admin.site.register(Post, PostAdmin)