from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from core.comment.models import Comment
from core.post.models import Post


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(), slug_field='public_id')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        if not Post.objects.filter(public_id=value.public_id).exists():
            raise ValidationError("Post does not exist")
        return value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super(CommentSerializer, self).update(instance, validated_data)
        return instance

    class Meta:
        model = Comment
        # List of all the fields that can be included in a
        # request or a response
        fields = ['id', 'post', 'author', 'body', 'edited',
                  'created', 'updated']
        read_only_fields = ['edited']

