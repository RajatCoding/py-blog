from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_posted', 'author']


admin.site.register(Post, PostAdmin)