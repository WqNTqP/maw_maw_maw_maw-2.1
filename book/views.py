from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serialixers import SnippetSerializers
from .serialixers import AuthorSerializers
from .serialixers import BookSerializers
from .serialixers import CategorySerializers
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework import generics
from .serialixers import UserSerializer
# Create your views here.

# def put(self, request, pk, format=None):
#     Snippet = self.serializer_class.Meta.model.objects.get(id=pk)
#     serializer = SnippetSerializers(Snippet, request.data)
#     if serializer.is_valid();
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def patch(self, request, pk, format=None):
#     Snippet = self.serializer_class.Meta.model.objects.get(id=pk)
#     serializer = SnippetSerializers(Snippet, request.data partial=True)
#     if serializer.is_valid();
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def get(self, request, pk, *args, **kwargs):
#     try:
#         article = self.serializer_class.Meta.model.objects.get(id=pk)
#         serializer = self.serializer-class(article)
#         return Response(serializer.data)
#     except self.serializer_class.Meta.model.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)



class Snippet (ModelViewSet):
    serializer_class = SnippetSerializers

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = SnippetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        Snippet = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = SnippetSerializers(Snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        Snippet = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = SnippetSerializers(Snippet, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            article = self.serializer_class.Meta.model.objects.get(id=pk)
            serializer = self.serializer_class(article)
            return Response(serializer.data)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk,*args,**kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Author (ModelViewSet):
    serializer_class = AuthorSerializers

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        Author = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = AuthorSerializers(Author, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        Author = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = AuthorSerializers(Author, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            article = self.serializer_class.Meta.model.objects.get(id=pk)
            serializer = self.serializer_class(article)
            return Response(serializer.data)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk,*args,**kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Book (ModelViewSet):
    serializer_class = BookSerializers

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        Book = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = BookSerializers(Book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        Book = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = BookSerializers(Book, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            article = self.serializer_class.Meta.model.objects.get(id=pk)
            serializer = self.serializer_class(article)
            return Response(serializer.data)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk,*args,**kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Category (ModelViewSet):
    serializer_class = CategorySerializers

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        Category = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = CategorySerializers(Category, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        Category = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = CategorySerializers(Category, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            article = self.serializer_class.Meta.model.objects.get(id=pk)
            serializer = self.serializer_class(article)
            return Response(serializer.data)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk,*args,**kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
