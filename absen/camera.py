import cv2
from mtcnn_cv2 import MTCNN
import numpy as np
from django.contrib.auth.models import User
from django.http import JsonResponse
from . import views
import json
from . models import User as user

from . models import data_wajah as wajah

import time

from . import views

#face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
detector = MTCNN()

class VideoCamera(object):
	def __init__(self):
		self.cam = cv2.VideoCapture(0)
		self.cam.set(3, 700) # set video width
		self.cam.set(4, 550) # set video height
		self.count = 0
		self.status = 1

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
			bounding_box = person['box']
			keypoints = person['keypoints']
			self.count += 1
			cv2.rectangle(frame,
						(bounding_box[0], bounding_box[1]),
						(bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
						(34, 255, 140),
						4)
			if self.count <=30:
				nama_file = "{0}_{1}_{2}_{3}-".format(data.id_user,data.username,data.first_name,data.last_name) + str(self.count) + ".jpg"
				cv2.imwrite("dataset/" + nama_file, gray[bounding_box[1]:bounding_box[1]+bounding_box[3],bounding_box[0]: bounding_box[0] + bounding_box[2]])
				record = wajah(nama_file=nama_file,id_user_id=data.id_user)
				record.save()
			else:
				data.is_face_recorded = 1
				data.save()
				self.cam.stream.release()
				break

		frame_flip = cv2.flip(frame, 15)
		ret, frame = cv2.imencode('.jpg', frame_flip)


		return frame.tobytes()