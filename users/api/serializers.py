from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")    
        instance.username = validated_data.get("username")    
        instance.email = validated_data.get("email")    
        instance.set_password(validated_data.get("password"))

        instance.save()    
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) > 0:
            if self.instance is not None and self.instance.username != data:       
                raise serializers.ValidationError("Ya existe ese username")
        return data

    def validate_email(self, data):
        users = User.objects.filter(email=data)
        if len(users) > 0:
            if self.instance is not None and self.instance.email != data:       
                raise serializers.ValidationError("Ya existe ese email")
        return data










