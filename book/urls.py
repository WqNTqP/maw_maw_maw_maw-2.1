from django.urls import path
from .views import SnippetViewSet, AuthorViewSet, BookViewSet, CategoryViewSet

urlpatterns = [
    path('', SnippetViewSet.as_view({'get': 'list'})),  # Add this line
    path('snippet', SnippetViewSet.as_view({'get': 'list', 'post': 'post'})),
    path('author', AuthorViewSet.as_view({'get': 'list', 'post': 'post'})),
    path('book', BookViewSet.as_view({'get': 'list', 'post': 'post'})),
    path('category', CategoryViewSet.as_view({'get': 'list', 'post': 'post'})),
]