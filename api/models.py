from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Dr. {self.doctor.name} - {self.date} {self.time}"
