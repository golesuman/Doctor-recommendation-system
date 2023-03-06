from api.views.hospital_view import PredictDoctorView
from api.views.with_naive_bayes import PredictDoctorWithNaiveBayesView
from django.urls import path

urlpatterns = [
    path("recommend-doctor", view=PredictDoctorView.as_view(), name="recommend-doctor"),
    path("recommend", view=PredictDoctorWithNaiveBayesView.as_view(), name="naive-bayes"),
]
