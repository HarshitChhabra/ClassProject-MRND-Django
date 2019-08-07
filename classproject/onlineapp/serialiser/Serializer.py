from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from onlineapp.models import College,MockTest1,Student
from django.shortcuts import get_object_or_404

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id','name', 'location', 'acronym', 'contact',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out',)

class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('problem1','problem2','problem3','problem4',)

class StudentDetailSerializer(serializers.ModelSerializer):

    mocktest1 = MockTestSerializer(read_only=False,many=False)

    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out','mocktest1')

    def create(self, validated_data):
        mocktest_data = validated_data.pop('mocktest1')
        college = get_object_or_404(College,id=self.context.get('pk'))
        student = Student.objects.create(**validated_data,college=college)
        total = mocktest_data['problem1'] + mocktest_data['problem2'] + mocktest_data['problem3'] + mocktest_data['problem4']
        mocktest = MockTest1.objects.create(**mocktest_data,total=total,student= student)
        return student


