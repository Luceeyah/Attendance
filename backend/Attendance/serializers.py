from itertools import product
from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Attendance
        # fields =[ 'staff_Id', 'gender', 'designation',]
        fields ='__all__'