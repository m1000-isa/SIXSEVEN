from django.contrib import admin

# Register your models here.
from .models import Category, Post, Coment

class ComentItemInIiene(admin.TabularInline):
    model = Coment
    raw_id_fields = ['Post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ('title', 'category', 'created_at', 'status')
    list_filter = ['category', 'created_at', 'status']
    inlines = [ComentItemInIiene]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title')

class ComentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Coment, ComentAdmin)