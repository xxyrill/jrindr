from rest_framework import status
from core.fixture.user import user
from core.fixture.post import post
from core.fixture.comment import comment
from rest_framework.test import APIClient


class TestCommentViewSet:
    # The comment resource is nested under the post resource
    endpoint = '/api/post/'

    #TEST TO RETRIEVE COMMENTS AS AUTHENTICATED USERS
    def test_list(self, client, user, post, comment):
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get(self.endpoint +
                              str(post.public_id) + '/comment/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user, post, comment):
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get(f'/api/post/{post.public_id}/comment/{comment.public_id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == comment.public_id.hex
        assert response.data['body'] == comment.body
        assert response.data['author']['id'] == comment.author.public_id.hex

    # TEST FOR COMMENT CREATION, UPDATING, AND DELETION
    def test_create(self, client, user, post):
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'body': 'Test Comment Body',
            'author': user.public_id.hex,
            'post': post.public_id.hex
        }
        response = client.post(self.endpoint +
                               str(post.public_id) +
                               '/comment/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['body'] == data['body']
        assert response.data['author']['id'] == user.public_id.hex

    def test_update(self, client, user, post, comment):
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            'body': 'Test Comment Body Updated',
            'author': user.public_id.hex,
            'post': post.public_id.hex
        }
        response = client.put(self.endpoint +
                              str(post.public_id) +
                              '/comment/' +
                              str(comment.public_id) +
                              '/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == data['body']

    def test_delete(self, client, user, post, comment):
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint +
                                 str(post.public_id) +
                                 '/comment/' +
                                 str(comment.public_id) + '/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_list_anonymous(self, client, post, comment):
        response = client.get(self.endpoint +
                              str(post.public_id) +
                              '/comment/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve_anonymous(self, client, post, comment):
        response = client.get(self.endpoint +
                              str(post.public_id) +
                              '/comment/' +
                              str(comment.public_id) + '/')
        assert response.status_code == status.HTTP_200_OK

    # TESTING TO ENSURE ANONYMOUS USER CANT CREATE, UPDATE, & DELETE COMMENTS
    def test_create_anonymous(self, client, post):
        data= {}
        response = client.post(self.endpoint +
                               str(post.public_id) +
                               '/comment/',
                               data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_anonymous(self, client, post, comment):
        data = {}
        response = client.post(self.endpoint +
                               str(post.public_id) + '/comment/' +
                               str(comment.public_id) + '/', data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymous(self, client, post, comment):
        response = client.delete(self.endpoint +
                                 str(post.public_id) + '/comment/' +
                                 str(comment.public_id) + '/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED










