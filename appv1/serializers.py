from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.exceptions import APIException

from .models import CustomUser, Fan, Presentation, Darslik, IshReja

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class FanSerializer(ModelSerializer):
    class Meta:
        model = Fan
        fields = '__all__'

class PresentationSerializer(ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class DarslikSerializer(ModelSerializer):
    class Meta:
        model = Darslik
        fields = '__all__'

class IshRejaSerializer(ModelSerializer):
    class Meta:
        model = IshReja
        fields = '__all__'
