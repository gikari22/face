from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http.response import StreamingHttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from absen.camera import *

from django.forms import formset_factory

from . models import kelas_guru as KelasModel

from . models import list_kelas_murid

from . models import absen as kuisModel

from . models import data_wajah as wajah

from . models import User as user

from . forms import LoginForm, SignUpForm1, SignUpForm2, kelas_guru, edit_teacher,edit_student, kelasguruForm, absen, absenform, joinkelas, joinkelasForm

import cv2
import numpy as np

def register_student(request):
	msg = None
	if request.method == 'POST':
		form = SignUpForm1(request.POST)
		if form.is_valid():
			form.save()
			msg = 'user created'
			return redirect('index')
		else:
			print('here')
			msg = 'form is not valid'
			return render(request, 'register_student.html', {'form': form, 'msg' : msg})
	else:
		form = SignUpForm1()
		return render(request, 'register_student.html', {'form': form, 'msg' : msg})

def register_teacher(request):
	msg = None
	if request.method == 'POST':
		form = SignUpForm2(request.POST)
		if form.is_valid():
			form.save()
			msg = 'user created'
			return redirect('index')
		else:
			print('here')
			msg = 'form is not valid'
			return render(request, 'register_teacher.html', {'form': form, 'msg' : msg})
	else:
		form = SignUpForm2()
		return render(request, 'register_teacher.html', {'form': form, 'msg' : msg})

def index(request):
	form = LoginForm(request.POST or None)
	msg = None
	if request.method == 'POST':
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			#if user is not None and user.is_admin:
				#login(request, user)
				#return redirect('adminpage')
			if user is not None and user.is_student:
				login(request, user)
				return redirect('student')
			elif user is not None and user.is_teacher:
				login(request, user)
				return redirect('teacher')
			else:
				#msg = 'invalid credential'
				return redirect('index')
		else:
			msg = 'error validation'
	return render(request, 'index.html', {'form': form, 'msg' : msg})


def home(request):
	return render(request, 'home.html')

def role(request):
	return render(request, 'role.html')

def student(request):
	form = edit_student()

	current_user = request.user
	#mur = muridModel.objects.get(id_user=current_user.id_user)
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	return render(request, 'student.html',{'lis' : lis, 'form': form})

def teacher(request):
	form = edit_teacher()

	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	return render(request, 'teacher.html',{'lis' : lis, 'form': form})

def kelas_guruku(request, id_kelas_guru = None):
	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	if id_kelas_guru:
		kls = KelasModel.objects.get(id_kelas_guru=id_kelas_guru)
		kuis = kuisModel.objects.filter(id_kelas_guru=id_kelas_guru)
		return render(request, 'kelas_guru.html', {'kls': kls, 'lis' : lis, 'kuis' : kuis})
	else:
		return redirect('teacher')

def kelas_muridku(request, id_kelas_guru = None):
	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	if id_kelas_guru:
		kls = KelasModel.objects.get(id_kelas_guru=id_kelas_guru)
		kuis = kuisModel.objects.filter(id_kelas_guru=id_kelas_guru)
		return render(request, 'kelas_murid.html', {'kls': kls, 'lis' : lis, 'kuis' : kuis})
	else:
		return redirect('student')
	
def create(request):
	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	if request.method == 'POST':
		form = kelas_guru(request.POST)
		if form.is_valid():
			class_name = form.cleaned_data.get('class_name')
			qdetail = form.cleaned_data.get('qdetail')
			id_user = form.cleaned_data.get('id_user')
			form.save()
			return redirect('teacher')
		else:
			print(form.errors)
			form = kelasguruForm()
			return render(request, 'create.html', { 'form': form, 'lis' : lis})
	else:
		form = kelasguruForm()
		return render(request, 'create.html', {'form': form, 'lis' : lis})

def semua_kelas_guru(request):
	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	return render(request, 'semua_kelas_guru.html',{'lis' : lis})

def semua_kelas_murid(request):
	current_user = request.user
	id_user_get = current_user.id_user
	guru = KelasModel.objects.all()
	mur = list_kelas_murid.objects.filter(id_user=id_user_get)
	lis = []
	for i in mur:
		clss = KelasModel.objects.filter(id_kelas_guru=i.id_kelas_guru_id).values()
		lis.append(clss)
	return render(request, 'semua_kelas_murid.html',{'lis' : lis})

def buatabsen(request, id_kelas_guru = None):
	current_user = request.user
	lis = KelasModel.objects.filter(id_user=current_user.id_user)
	if request.method == 'POST':
		form = absen(request.POST)
		if form.is_valid():
			nama_absen = form.cleaned_data.get('nama_kuis')
			id_kelas_guru = form.cleaned_data.get('id_kelas_guru')
			form.save()
			return redirect('semua_kelas_guru')
		else:
			print(form.errors)
			return redirect('buatabsen')
	else:
		if id_kelas_guru:
			kls = KelasModel.objects.get(id_kelas_guru=id_kelas_guru)
			form = absenform()
			return render(request, 'buatabsen.html', {'form': form, 'lis' : lis, 'kls' : kls})
		else:
			form = absen()
			return render(request, 'buatabsen.html', {'form': form, 'lis' : lis})


def logout(request):
    return render(request, 'index.html')

def enroll(request):
	current_user = request.user
	if request.method == 'POST':
		form = joinkelas(request.POST)
		if form.is_valid():
			form.save()
			id_kelas_guru = form['id_kelas_guru'].value()
			jml = list_kelas_murid.objects.filter(id_kelas_guru=id_kelas_guru).count()
			print(jml)
			klsup = KelasModel.objects.get(id_kelas_guru=id_kelas_guru)
			klsup.jumlah_peserta = jml
			klsup.save()
			return redirect('student')
		else:
			print(form.errors)
			return redirect('enroll')
	else:
		#form = joinkelasForm()
		return render(request, 'enroll.html')

def classroom(request):
	return render(request, 'class.html')

def gen(camera,username):
	while True:
		frame = camera.get_frame(username)
		yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_stream(request):
	current_user = request.user
	id_user = current_user.id_user
	return StreamingHttpResponse(gen(VideoCamera(),id_user),
      	content_type='multipart/x-mixed-replace; boundary=frame')

def record(request):
	return render(request,"record.html")