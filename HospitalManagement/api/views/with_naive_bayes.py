# from django.shortcuts import render
from api.serializers.doctor_serializer import HospitalSerializer, SpecialtySerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.stop_words import specialties
from utils.text_processing import  is_input_valid
from utils.naive_bayes_algorithm import give_disease_with_naive_bayes

class PredictDoctorWithNaiveBayesView(APIView):
    class InputSerializer(serializers.Serializer):
        symptoms = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        specialty = SpecialtySerializer()
        phone_number = serializers.CharField()
        email = serializers.CharField()
        hospital = HospitalSerializer()

    def post(self, request, *args, **kwargs):
        result = []
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        symptoms = request.data["symptoms"]
        if not is_input_valid(symptoms):
            return Response(
                data={"data": "Please enter valid text"},
                status=status.HTTP_200_OK,
            )

        diseases = give_disease_with_naive_bayes(input_text=symptoms)

        if not diseases:
            return Response(
                data={
                    "data": "Sorry we couldn't find you a doctor. Sorry for inconvenience."
                },
                status=status.HTTP_200_OK,
            )
        # for disease in diseases:
        #     for key, values in specialties.items():
        #         if disease in values:
        #             result.append(key)

        # return Response(data={"data": set(result)}, status=status.HTTP_200_OK)
        return Response(data = diseases)