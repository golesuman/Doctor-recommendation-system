from api.models.hospital import Doctor


def get_doctor(disease):
    doctor = Doctor.objects.filter(specialty__disease=disease).first()
    return doctor
