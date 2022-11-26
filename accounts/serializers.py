from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        read_only_fields = "id"
