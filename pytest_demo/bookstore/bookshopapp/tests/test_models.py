from ..models import User
import pytest


@pytest.mark.django_db
class TestModels:
    """
    This class will test my User model
    """
    def test_is_email_registered(self):
        user = User.objects.create(
            fname='prajyot', lname='pomannawar', email='prajyot@gmail',
            password='prajyot@123', mobile='9552566838'
        )
        assert user.is_email_registered == "prajyot@gmail"
