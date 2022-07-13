import cv2
import numpy as np
import os
from mtcnn_cv2 import MTCNN
import datetime

from . models import list_kelas_murid as kel

from .models import User as user

from . models import data_wajah as wajah

from . models import data_absen as absen

from . models import absen as absin

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = MTCNN()
recognizer.read('trainer/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX

class FaceRecog(object):
	def __init__(self):
		self.font = cv2.FONT_HERSHEY_SIMPLEX
		self.ids = 0
		self.cam = cv2.VideoCapture(0)
		self.cam.set(3, 800) # set video width
		self.cam.set(4, 600) # set video height
		self.abs = False

	def __del__(self):
		self.cam.release()

	def absent(self, id_user, id_absen):

		ret, img = self.cam.read()

		idusr = id_user
		
		idabs = id_absen

		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		faces = detector.detect_faces(img)

		usr = user.objects.get(id_user=idusr)

		for person in faces:
			box = person['box']
			keypoints = person['keypoints']
			conf = person['confidence']
			#print(conf)
			x, y, w, h = box[0], box[1], box[2], box[3]
			'''cv2.rectangle(img,
						(x, y),
						(x+w, y + h),
						(34, 255, 140),
						4)'''
			idusr, confidence = recognizer.predict(gray[y:y+h,x: x + w])
			absn = absen.objects.filter(id_absen_id=idabs, id_user_id=idusr).count()
			if (confidence <= 50):
				idusr = idusr
				if idusr == usr.id_user and self.abs == False and absn < 1:
					if w >=200:
						nama_file = "{0}_{1}_{2}_".format(usr.username,usr.first_name,usr.last_name)+ "Hadir" + ".jpg"
						cv2.imwrite("absen/" + nama_file, img)
						absen.objects.create(file_absen="absen/" +nama_file,waktu_absen=datetime.datetime.now(),id_user_id=idusr,id_absen_id=idabs)
						#confidence = "  {0}%".format(round(100 - confidence))
						jml = absen.objects.filter(id_absen_id=idabs).count()
						print(jml)
						isi = absin.objects.get(id_absen=idabs)
						isi.jumlah_terisi = jml
						isi.save()
						self.abs = True
						cv2.putText(img,"Absen Berhasil", (x+5,y-5), self.font, 1, (255,255,255), 2)
					
					else :
						cv2.putText(img,"Dekatkan Wajah", (x+5,y-5), self.font, 1, (255,255,255), 2)
			else :
				cv2.putText(img,"Tidak Dikenali", (x+5,y-5), self.font, 1, (255,255,255), 2)
				idusr = 0  


		ret, img = cv2.imencode('.jpg', img)

		return img.tobytes()