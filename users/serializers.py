from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'password',)
