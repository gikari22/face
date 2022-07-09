import cv2
import numpy as np
from PIL import Image
import os
from mtcnn_cv2 import MTCNN
from . models import list_kelas_murid as kel

from . models import data_wajah as wajah

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = MTCNN()

class traindat(object):
	def __init__(self):
		self.arg = ""

	def getImagesAndLabels(id_kelas):
		kelas = id_kelas
		print(kelas)
		lis = kel.objects.filter(id_kelas_murid=kelas) 

		path = "dataset/"
		grup_sis_image = []

		for i in lis:
			path_sis = wajah.object.get(id_user=i.id_user_id).values()
			fix_path = path+path_sis.nama_file
			grup_sis_image.append(fix_path)

		#imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
		faceSamples=[]
		ids = []

		return grup_sis_image
		