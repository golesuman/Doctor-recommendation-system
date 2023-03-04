from rest_framework import serializers, status

# from rest_framework import


class SpecialtySerializer(serializers.Serializer):
    name_of_specialty = serializers.CharField()
    disease = serializers.CharField()


class HospitalSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
