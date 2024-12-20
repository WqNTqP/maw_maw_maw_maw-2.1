from django.urls import path, include
from .views import (Snippet)
from .views import (Author)
from .views import (Book)
from .views import (Category)
from .views import UserDetail

urlpatterns = [
    path('snippet', Snippet.as_view({
        'get':'list',
        'post':'post',
    })),
    path('snippet/<int:pk>/',Snippet.as_view({
        'put':'put',
        'patch':'patch',
        'delete':'delete',
        'get' : 'get',
    })),
    path('author', Author.as_view({
        'get':'list',
        'post':'post',
    })),
        path('author/<int:pk>/',Author.as_view({
        'put':'put',
        'patch':'patch',
        'delete':'delete',
        'get' : 'get',
    })),
    path('book', Book.as_view({
        'get':'list',
        'post':'post',
    })),
    path('book/<int:pk>/',Book.as_view({
        'put':'put',
        'patch':'patch',
        'delete':'delete',
        'get' : 'get',
    })),
    path('category', Category.as_view({
        'get':'list',
        'post':'post',
    })),
    path('category/<int:pk>/',Category.as_view({
        'put':'put',
        'patch':'patch',
        'delete':'delete',
        'get' : 'get',
    })),
    path('api/user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

# try