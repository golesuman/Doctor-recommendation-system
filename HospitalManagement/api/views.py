# from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.recommendation import RecommendDoctor

recommend = RecommendDoctor()


class PredictDoctorView(APIView):
    def post(self, request, *args, **kwargs):
        no_of_doctors = request.data["noOfDoctors"]
        symptoms = request.data["symptoms"]
        result = recommend.give_disease(input_text=symptoms, no_of_doctors=no_of_doctors)
        return Response({"data": result}, status.HTTP_200_OK)
