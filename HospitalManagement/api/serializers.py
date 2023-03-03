from rest_framework import serializers, status

# from rest_framework import


class DoctorSerializer(serializers.Serializer):
    name = serializers.CharField()
    specialty = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()
    hospital = serializers.CharField()


class SpecialtySerializer(serializers.Serializer):
    name_of_specialty = serializers.CharField()
    disease = serializers.CharField()


class HospitalSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
