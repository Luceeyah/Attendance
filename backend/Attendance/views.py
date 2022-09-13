

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from Attendance import serializers

from Attendance.models import Attendance

from Attendance.serializers import AttendanceSerializer

from rest_framework import status



@api_view(['GET'])
def attendance_list(request):

    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer( attendance ,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def attendance_create(request):

        serializer= AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET'])
def attendance_Detail (request,id):
    try:
        attendance = Attendance.objects.get(pk=id) 
    except Attendance.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    serializer =AttendanceSerializer(attendance, many=False)
    return Response(serializer.data)


#update single attendance
@api_view(['PUT'])
def update_attendance(request,id,format=None):
    try:
        attendance = Attendance.objects.get(pk=id)
    except Attendance.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = AttendanceSerializer(attendance, data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Delete single Tour

@api_view(['DELETE'])
def delete_attendance(request, id):
        try:
            attendance = Attendance.objects.get(pk=id)
        except Attendance.DoesNotExist:
            return Response(status =status.HTTP_404_NOT_FOUND)
        attendance.delete()
        return Response('attendance deleted successfully' , status=status.HTTP_204_NO_CONTENT)