from django.urls import path

# import class View
from . import views

urlpatterns = [
    #path('login/', views.LoginView, name='login'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('role/', views.role, name='role'),
    path('class/', views.classroom, name='class'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('student/', views.student, name='student'),
    path('record/', views.record, name='record'),
    path('enroll/', views.enroll, name='enroll'),
    path('teacher/', views.teacher, name='teacher'),
    path('create/', views.create, name='create'),
    path('semua_kelas_guru/', views.semua_kelas_guru, name='semua_kelas_guru'),
    path('semua_kelas_murid/', views.semua_kelas_murid, name='semua_kelas_murid'),
    path('absensih/', views.absensih, name='absensih'),
    path('absensih/<int:id_absen>/<int:id_kelas_guru>/', views.absensih, name='absensih'),
    path('buatabsen/', views.buatabsen, name='buatabsen'),
    path('buatabsen/<int:id_kelas_guru>/', views.buatabsen, name='buatabsen'),
    path('laporan/<int:id_absen>/', views.laporan, name='laporan'),
    path('kelas_guruku/', views.kelas_guruku, name='kelas_guruku'),
    path('kelas_guruku/<int:id_kelas_guru>/', views.kelas_guruku, name='kelas_guruku'),
    path('kelas_muridku/', views.kelas_muridku, name='kelas_muridku'),
    path('kelas_muridku/<int:id_kelas_guru>/', views.kelas_muridku, name='kelas_muridku'),
    path('video_stream', views.video_stream, name='video_stream'),
    path('video_absen/<int:id_absen>/', views.video_absen, name='video_absen'),
]