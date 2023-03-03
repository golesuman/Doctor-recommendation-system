from api.models import Doctor


def get_doctor(disease):
    doctor = Doctor.objects.filter(specialty__disease=disease)
    return doctor
