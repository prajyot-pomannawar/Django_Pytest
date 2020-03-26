from django.urls import reverse, resolve


class TestUserUrls:
    """
    This class will test all urls related to user side
    """
    def test_view_single_user_url(self):
        path = reverse('view_single_user', kwargs={'id': 1})
        assert resolve(path).view_name == 'view_single_user'

    def test_view_all_user_url(self):
        path = reverse('view_all_users')
        assert resolve(path).view_name == 'view_all_users'

    def test_edit_user_url(self):
        path = reverse('edit_user', kwargs={'id': 1})
        assert resolve(path).view_name == 'edit_user'

    def test_delete_user_url(self):
        path = reverse('delete_user', kwargs={'id': 1})
        assert resolve(path).view_name == 'delete_user'

    def test_register_user_url(self):
        path = reverse('create_user')
        assert resolve(path).view_name == 'create_user'


class TestBookUrls:
    """
    This class will test all urls related to Book side
    """
    def test_view_single_book_url(self):
        path = reverse('view_single_book', kwargs={'id': 1})
        assert resolve(path).view_name == 'view_single_book'

    def test_view_all_books_url(self):
        path = reverse('view_all_books')
        assert resolve(path).view_name == 'view_all_books'

    def test_create_book_url(self):
        path = reverse('create_book')
        assert resolve(path).view_name == 'create_book'

    def test_edit_book_url(self):
        path = reverse('edit_book', kwargs={'id': 1})
        assert resolve(path).view_name == 'edit_book'

    def test_delete_book_url(self):
        path = reverse('delete_book', kwargs={'id': 1})
        assert resolve(path).view_name == 'delete_book'

    def test_search_book_url(self):
        path = reverse('search_book')
        assert resolve(path).view_name == 'search_book'
