import pytest
from rest_framework import status
from core.fixture.user import user


class TestAuthenticationViewset:
    endpoint = '/api/auth/'

    def test_login(self, client, user):
        data = {
            'email': user.email,  # change from user.username to user.email
            # because the login requires an email in Insomnia.
            # See OneNote for more details
            'password': 'test_password',
        }
        response = client.post(self.endpoint + 'login/', data)

        if response.status_code != status.HTTP_200_OK:
            print(f'Response status code: {response.status_code}')
            print(f'Response data: {response.data}')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['user'] ['id'] == user.public_id.hex
        assert response.data['user'] ['username'] == user.username
        assert response.data['user'] ['email'] == user.email

    @pytest.mark.django_db
    def test_register(self,client):
        data = {
            'username': 'johndoe',
            'email': 'johndoe@yopmail.com',
            'password': 'test_password',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        response = client.post(self.endpoint + 'register/', data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_refresh(self, client, user):
        data = {
            'email': user.email,
            'password': 'test_password',
        }
        response = client.post(self.endpoint + 'login/', data)
        assert response.status_code == status.HTTP_200_OK
        data_refresh = {
            'refresh': response.data['refresh']
        }
        response = client.post(self.endpoint + 'refresh/', data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']






















