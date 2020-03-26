# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from bookshopapp.models import User, Book, Log
from .serializer import BookSerializer, UserSerializer, LogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

book = Book()
user = User()


# Create your views here.
class BookList(APIView):
    def get(self, request, format=None):
        """
        Method which returns list of Books
        """
        serializer = BookSerializer(book.return_book(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Method Which creates new book and add it to database
        """
        serializer = BookSerializer(data=book.create_book(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewClass(APIView):

    def get_object(self, id):
        """
        Return details of single book with matching ID
        """
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id,  format=None):
        """
        Method Used to show only single book with matching id
        """
        serializer = BookSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        Method Used for updating book details
        """
        serializer = BookSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """
        Method for deleting specific book
        """
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    def get(self, request, format=None):
        """
        Method will return all registered Users
        """
        serializer = UserSerializer(user.get_users(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Method will create new user object and add it to database
        """
        for current_user in user.get_user_email():
            if current_user.email == request.data.get('email'):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewClass(APIView):

    def get_object(self, id):
        """
        Method will fetch and return single user with matching id.
        """
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """
        Method will fetch and return single user with matching id.
        """
        serializer = UserSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        User can update his/her information except email.
        If email is also changed by user then Bad request status is shown
        else updated data is stored to db
        """
        for current_user in user.get_user_email():
            if current_user.email != request.data.get('email'):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """
        Method to delete specified user
        """
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchBook(APIView):
    def post(self, request, format=None):
        """
        Method to search the book by entering title.
        For searching a book, first it checkes whether user is logged in or not
        If yes, then only it finds books containing key word entered by user,
        returns all books containing that keyword in their title.
        While doing this, also maintains the log. Which user searched which book.
        """
        for u in user.get_users():
            if u.email == request.data.get('email') and u.password == request.data.get('password'):
                serializer1 = BookSerializer(Book.objects.filter(title__contains=request.data.get('title').upper()),
                                             many=True)
                log_data = {
                    'keyword': request.data.get('title'),
                    'user': u.id,
                }
                serializer2 = LogSerializer(data=log_data)
                if serializer2.is_valid():
                    serializer2.save()
                    return Response(serializer1.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
