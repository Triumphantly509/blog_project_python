from django.contrib import admin
from django.utils.html import format_html
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_published', 'image_tag')
    search_fields = ('title',)  
    list_filter = ('date_published',) 
    
     # Function to display image in admin
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return '-'
    image_tag.short_description = 'Image' 

admin.site.register(Post, PostAdmin)