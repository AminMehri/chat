from rest_framework import serializers



class AddConversationSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=2048)
    usersId = serializers.CharField()