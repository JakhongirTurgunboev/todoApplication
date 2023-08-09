from django.contrib.auth.hashers import make_password

from todo.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Leave empty if no change needed",
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Task
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
        write_only_fields =('password',)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(TaskSerializer, self).create(validated_data)

    def update(self, validated_data, instance=None):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(TaskSerializer, self).update(instance=instance, validated_data=validated_data)