from django.urls import path
from api.views import PredictDoctorView

urlpatterns = [
    path("recommend-doctor", view=PredictDoctorView.as_view(), name="recommend-doctor"),
]