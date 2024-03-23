from djoser.serializers import UserCreateSerializer as UserSerializer

# ----xxxx----

class UserCreateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']