from django.urls import path, include
from .views import (Snippet)
from .views import (Author)
from .views import (Book)
from .views import (Category)

urlpatterns = [
    path('snippet', Snippet.as_view({
        'get':'list',
        'post':'post',
    })),
    path('<int:pk>', Snippet.as_view({
        'put':'put',
        'patch' : 'patch',
        'get' :'get',
    })),
    path('author', Author.as_view({
        'get':'list',
        'post':'post',
    })),
    path('book', Book.as_view({
        'get':'list',
        'post':'post',
    })),
    path('category', Category.as_view({
        'get':'list',
        'post':'post',
    }))
]