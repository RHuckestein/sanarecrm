from rest_framework import serializers
from refferal_accounts.models import RefferalAccount


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefferalAccount
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'phone', 'email')
