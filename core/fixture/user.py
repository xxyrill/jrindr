import pytest
from core.user.models import User

data_user = {
    'username': 'test_user',
    'email': 'test@gmail.com',
    'first_name': 'Test',
    'last_name': 'User',
    'password': 'test_password',
}
@pytest.fixture
def user(db) -> User:
    user = User.objects.create_user(
        username=data_user['username'],
        email=data_user['email'],
        first_name=data_user['first_name'],
        last_name=data_user['last_name'],
        password=data_user['password']
    )
    return user