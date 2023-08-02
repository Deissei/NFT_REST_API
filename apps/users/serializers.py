from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'avatar',
            'cover_image',
            'display_name',
            'balance',
            'url',
            'email',
            'description',
            'cart_user',
            'instagram',
            'telegram',
            'facebook',
        )
        read_only_fields = (
            'id',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'display_name',
            'password',
            'email',
        )
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        password = validated_data['password']
        if not password:
            raise serializers.ValidationError("[ERROR]!: Not Password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        if not user.avatar:
            user.avatar = "default_images/360_F_209370065_JLXhrc5inEmGl52SyvSPeVB23hB6IjrR.jpg"
            user.save()
        
        return user


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    new_password1 = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'password',
            'new_password1',
            'new_password2',
        )
    
    def validate(self, attrs):
        new_password1 = attrs.get('new_password1')
        new_password2 = attrs.get('new_password2')
        if new_password1 != new_password2:
            raise serializers.ValidationError("[ERROR!]: The new passwords don't match!")
        return attrs

    def update(self, instance, validated_data):
        new_password = validated_data['new_password1']
        instance.set_password(new_password)
        instance.save()
        return instance
    
    def validate_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("[ERROR!]: The old password is incorerect!")
        return value
    
    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password1']
        user.set_password(new_password)
        user.save()
        return user
