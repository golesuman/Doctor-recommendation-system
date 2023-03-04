# from django.shortcuts import render
from api.serializers.doctor_serializer import HospitalSerializer, SpecialtySerializer
from api.services.get_doctor_service import get_doctor
from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.recommendation import give_disease


class PredictDoctorView(APIView):
    class InputSerializer(serializers.Serializer):
        noOfDoctors = serializers.IntegerField()
        symptoms = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        specialty = SpecialtySerializer()
        phone_number = serializers.CharField()
        email = serializers.CharField()
        hospital = HospitalSerializer()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        diseases = give_disease(input_text=request.data["symptoms"])
        queryset = get_doctor(diseases[0])
        serializer = self.OutputSerializer(queryset, many=True)
        # return Response({"data": serializer.data}, status.HTTP_200_OK)
        return Response({"data": diseases}, status.HTTP_200_OK)