from rest_framework.serializers import ModelSerializer
from web_app.models import WalletCrypto

class WalletCryptoSerializer(ModelSerializer):
    class Meta:
        model = WalletCrypto
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

