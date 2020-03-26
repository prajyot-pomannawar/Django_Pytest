from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'books', views.BookList.as_view(), name='view_all_books'),
    url(r'addbook', views.BookList.as_view(), name='create_book'),
    url(r'viewbook/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='view_single_book'),
    url(r'editbook/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='edit_book'),
    url(r'deletebook/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='delete_book'),
    url(r'searchbook', views.SearchBook.as_view(), name='search_book'),
    url(r'users', views.UserList.as_view(), name='view_all_users'),
    url(r'adduser', views.UserList.as_view(), name='create_user'),
    url(r'viewuser/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='view_single_user'),
    url(r'edituser/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='edit_user'),
    url(r'deleteuser/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='delete_user'),
]
