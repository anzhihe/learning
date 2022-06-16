from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Group, Student


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')



class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'group')
