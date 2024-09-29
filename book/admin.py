from django.contrib import admin
from .models import Book, Author, Category,Snippet
# Register your models here.



@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = [ 'id','name','description']
    search_fields = ['name', 'description']
    list_filter = ['name']

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Snippet)
#admin.site.register(Category)

