from django.contrib.auth.models import Group, User
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'groups',
            ]
    


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groupfields = [
            'url',
            'name'
        ]