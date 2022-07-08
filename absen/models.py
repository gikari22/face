from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	id_user = models.BigAutoField(primary_key=True)
	is_student = models.BooleanField('Is Student', default = False)
	is_teacher = models.BooleanField('Is Teacher', default = False)
	is_face_recorded = models.BooleanField('Is Teacher', default = False)

class kelas_guru(models.Model):
	id_kelas_guru = models.BigAutoField(primary_key=True)
	nama_kelas = models.CharField(max_length=100)
	deskripsi_kelas = models.TextField()
	jumlah_peserta = models.IntegerField()
	id_user = models.ForeignKey(User, on_delete=models.CASCADE)

	objects = models.Manager()

class absen(models.Model):
	id_absen = models.BigAutoField(primary_key=True)
	nama_absen = models.CharField(max_length=100)
	waktu_mulai = models.TextField()
	waktu_selesai = models.TextField()
	jumlah_terisi = models.IntegerField()
	id_kelas_guru = models.ForeignKey(kelas_guru, on_delete=models.CASCADE)

	objects = models.Manager()

class data_absen(models.Model):
	id_data = models.BigAutoField(primary_key=True)
	file_absen = models.CharField(max_length=1000)
	waktu_absen = models.TextField()
	id_user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_absen = models.ForeignKey(absen, on_delete=models.CASCADE)

	objects = models.Manager()

class list_kelas_murid(models.Model):
	id_kelas_murid = models.BigAutoField(primary_key=True)
	id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	id_kelas_guru = models.ForeignKey(kelas_guru, on_delete=models.CASCADE)

	objects = models.Manager()

class data_wajah(models.Model):
	id_wajah = models.BigAutoField(primary_key=True)
	nama_file = models.CharField(max_length=1000)
	id_user = models.ForeignKey(User, on_delete=models.CASCADE)
		