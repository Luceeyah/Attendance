
from django.urls import path
from Attendance import views
# import Attendance 
# from .views import attendance_create

urlpatterns =[ 
    path('attendance', views.attendance_list),

    path('attendance/create', views.attendance_create),

    path('attendance/<int:id>/', views.attendance_Detail),

    path ('attendance/update/<int:id>/',views.update_attendance),

    path('attendance/delete/<int:id>/', views.delete_attendance)

]