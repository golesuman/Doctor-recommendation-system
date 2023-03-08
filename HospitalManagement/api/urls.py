from api.views.hospital_view import PredictDoctorView
from django.urls import path

from api.views.new_view import PredictDoctorAPI

urlpatterns = [
    path("recommend-doctor", view=PredictDoctorView.as_view(), name="recommend-doctor"),
    path("recommend-doc", view=PredictDoctorAPI.as_view(), name="recommend-doc")
]
