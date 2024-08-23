from rest_framework import status
from core.fixture.user import user
from core.fixture.post import post


class TestUserViewSet:
    endpoint = '/api/user/'

    def test_list(self, client, user):
        pass

    def test_retrieve(self, client, user):
        pass

    def test_create(self, client, user):
        pass

    def test_update(self, client, user):
        pass