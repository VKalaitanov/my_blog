from django.contrib import admin

from .models import Post, TagPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'tags']
    # exclude = ['tags', 'is_published']
    prepopulated_fields = {"slug": ("title",)}
    # filter_horizontal = ['tags']
    filter_vertical = ['tags']
    list_display = ('title', 'time_create', 'is_published')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_filter = ['is_published']
    save_on_top = True


admin.site.register(TagPost)
