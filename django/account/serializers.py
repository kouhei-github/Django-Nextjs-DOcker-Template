from rest_framework.serializers import ModelSerializer
from .models import Account
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'email',"shop_name", "username", "shop",
            "date_joined", "last_login", "is_admin",
            "is_active", "is_staff", "is_superuser",
            "shop_name", "password",
        )
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
