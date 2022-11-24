from rest_framework import serializers
from todo.models import Todo
from taggit.serializers import TagListSerializerField,TaggitSerializer


class CrudSerializer(TaggitSerializer,serializers.ModelSerializer):
    Tag=TagListSerializerField()
    
    class Meta:
        model=Todo
        fields=['Title','Description','duedate','Tag','status']

class UpdateTodoSerializer(TaggitSerializer,serializers.ModelSerializer):
    Tag=TagListSerializerField()
    class Meta:
        model=Todo
        fields=['Title','duedate','Tag']


class ViewTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'