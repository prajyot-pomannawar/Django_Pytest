from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('book', views.BookList.as_view(), name='book_list'),
    url(r'book/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='view_single_book'),
    # path('book/edit/<int:id>/', views.BookViewClass.as_view()),
    url(r'book/edit/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='edit_book'),
    # path('book/delete/<int:id>/', views.BookViewClass.as_view()),
    url(r'book/delete/(?P<id>[0-9]+)', views.BookViewClass.as_view(), name='delete_book'),
    path('user', views.UserList.as_view()),
    # path('user/<int:id>', views.UserViewClass.as_view()),
    url(r'user/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='view_single_user'),
    # path('user/edit/<int:id>', views.UserViewClass.as_view()),
    url(r'user/edit/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='edit_user'),
    # path('user/delete/<int:id>', views.UserViewClass.as_view()),
    url(r'user/delete/(?P<id>[0-9]+)', views.UserViewClass.as_view(), name='delete_user'),
    path('search', views.SearchBook.as_view()),
]
