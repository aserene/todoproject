from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #Which model will get serialized by the class
        model= Todo
        #which fields should be included in the output
        fields = ['id', 'subject', 'details']