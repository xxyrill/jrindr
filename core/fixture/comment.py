import pytest
from core.fixture.user import user
from core.fixture.post import post
from core.comment.models import Comment

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post,
                                  body='Test Comment Body')