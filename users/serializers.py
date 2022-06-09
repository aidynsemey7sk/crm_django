from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'password',)

    def to_representation(self, instance):
        data = super(UserRegistrationSerializer, self).to_representation(instance)
        user_tokens = RefreshToken.for_user(instance)
        tokens = {'refresh': str(user_tokens), 'access': str(user_tokens.access_token)}
        data = {
            "success": "true",
            # "data": data | tokens
        }
        return data
