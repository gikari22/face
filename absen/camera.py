import cv2
from mtcnn_cv2 import MTCNN
import numpy as np
from django.contrib.auth.models import User
from django.http import JsonResponse
from . import views
import json
from . models import User as user

from . models import data_wajah as wajah

from . models import data_absen as absen

import time

from . import views

#face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
detector = MTCNN()

class VideoCamera(object):
	def __init__(self):
		self.cam = cv2.VideoCapture(0)
		self.cam.set(3, 800) # set video width
		self.cam.set(4, 600) # set video height
		self.count = 0
		self.status = 1
		self.font = cv2.FONT_HERSHEY_SIMPLEX

	def __del__(self):
		self.cam.release()

	def get_frame(self, username):

		id_user = username

		__, frame = self.cam.read()
			
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#faces = face_detector.detectMultiScale(gray, 1.3, 5)

		result = detector.detect_faces(frame)
		for person in result:
			data = user.objects.get(id_user=id_user)
			box = person['box']
			keypoints = person['keypoints']
			conf = person['confidence']
			print(conf)
			x, y, w, h = box[0], box[1], box[2], box[3]
			'''cv2.rectangle(frame,
						(x, y),
						(x+w, y + h),
						(34, 255, 140),
						4)'''
			if self.count < 30 and w >=200 and len(result) == 1:
				self.count += 1
				cv2.putText(frame,"Tunggu", (x+5,y-5), self.font, 1, (255,255,255), 2)
				nama_file = "{0}_{1}_{2}_{3}-".format(data.id_user,data.username,data.first_name,data.last_name) + str(self.count) + ".jpg"
				cv2.imwrite("dataset/" + nama_file, frame)
				record = wajah(nama_file=nama_file,id_user_id=data.id_user)
				record.save()
			elif w < 200:
				cv2.putText(frame,"Dekatkan lagi wajah anda", (x+5,y-5), self.font, 1, (255,255,255), 2)
			elif self.count == 30 :
				#cv2.putText(frame,"Sudah di disimpan", (x+5,y-5), self.font, 1, (255,255,255), 2)
				cv2.putText(frame,"Silahkan Kembali", (x+5,y-5), self.font, 1, (255,255,255), 2)
				data.is_face_recorded = 1
				data.save()

		#frame_flip = cv2.flip(frame, 15)
		ret, frame = cv2.imencode('.jpg', frame)


		return frame.tobytes()