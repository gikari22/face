from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *
from django.forms import ModelForm

class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs=
			{"class": "form-control"}
		)
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs=
			{"class" : "form-control"}
		)
	)

class SignUpForm1(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(max_length=254, required=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_student')

class SignUpForm2(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(max_length=254, required=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_teacher')


class kelasguruForm(forms.Form):
	id_user = forms.ModelChoiceField(queryset=User.objects.all(),
		widget = forms.TextInput()
		)
	nama_kelas = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(
			
		)
	)
	deskripsi_kelas = forms.CharField(widget=forms.Textarea())

class kelas_guru(forms.ModelForm):
	
	class Meta:
		model = kelas_guru
		fields = ('nama_kelas', 'deskripsi_kelas', 'id_user', 'jumlah_peserta')

class absenform(forms.Form):
	id_kelas_guru = forms.ModelChoiceField(queryset=User.objects.all(),
		widget = forms.TextInput())

	nama_absen = forms.CharField(
		max_length=100, 
		widget=forms.TextInput())
	#banner_kelas = models.CharField(max_length=100)

	waktu_mulai = forms.DateTimeField(widget=forms.DateTimeInput(
		attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker'}))
	waktu_selesai = forms.DateTimeField(widget=forms.DateTimeInput())

class absen(forms.ModelForm):
	
	class Meta:
		model = absen
		fields = ('nama_absen', 'id_kelas_guru')

class joinkelasForm(forms.Form):
	id_user = forms.ModelChoiceField(queryset=User.objects.all(),
		widget = forms.TextInput()
		)
	id_kelas_guru = forms.CharField( 
		widget=forms.TextInput()
		)

class joinkelas(forms.ModelForm):
	
	class Meta:
		model = list_kelas_murid
		fields = ('id_user', 'id_kelas_guru')

class edit_teacher(forms.Form):
		first_name = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		last_name = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		username = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		email = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		password = forms.CharField(
		max_length=100, 
		widget=forms.PasswordInput(	))

class edit_student(forms.Form):
		first_name = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		last_name = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		username = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		email = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(	))

		password = forms.CharField(
		max_length=100, 
		widget=forms.PasswordInput(	))
		