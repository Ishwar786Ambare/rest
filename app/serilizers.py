from rest_framework import serializers


class EmpSeri(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    number = serializers.IntegerField()


class MyEmp(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    number = serializers.IntegerField()

