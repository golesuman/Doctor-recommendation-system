from django.urls import path
from api.views import PredictDoctorView

urlpatterns = [
    path('predict-disease/', PredictDoctorView.as_view(), 'predict-disease'),
    # path("", "")
]