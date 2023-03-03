from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class Specialty(models.Model):
    name_of_specialty = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name_of_specialty)

    class Meta:
        verbose_name = "specialty"
        verbose_name_plural = "specialties"


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name) + str(self.specialty)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
