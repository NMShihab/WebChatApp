from rest_framework import serializers

class LoginSerialzier(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerialzier(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()