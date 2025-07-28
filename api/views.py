from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer

@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def doctor_detail(request, id):
    try:
        doctor = Doctor.objects.get(pk=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=404)

@api_view(['POST'])
def book_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_appointments(request):
    doctor_id = request.GET.get('doctor_id')
    patient_id = request.GET.get('patient_id')

    if doctor_id:
        appointments = Appointment.objects.filter(doctor_id=doctor_id)
    elif patient_id:
        appointments = Appointment.objects.filter(patient_id=patient_id)
    else:
        appointments = Appointment.objects.none()

    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

