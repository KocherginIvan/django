from django.contrib import admin
from .models import Author, Book, Comment
# Register your models here.
admin.site.register(Author)
def clear_rating(modeladmin, request, queryset):
    queryset.update(img_href=None)


clear_rating.short_description = "Удалить Image"



class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'img_href', 'href', 'content']
    actions = [clear_rating]

admin.site.register(Book, BookAdmin)