from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import os
from glob import glob
import numpy as np
import pickle
from PIL import Image
import h5py
import csv

class ExtractImageFeatures():	
	def __init__(self, batch_size=25000):
		super(ExtractImageFeatures, self).__init__()
		self.batch_size = batch_size
		self.last_image = False
		if self.PathExists('data.csv'):
			print("data.csv already exists! Skipping extraction. Please ensure you have extracted all image features the first time.")
		else:
			print("Extacting image features...")	
			self.Extract()

	def PathExists(self, path):
		full_path = os.path.join(os.getcwd(), path)
		if os.path.exists(full_path):
			return True
		return False

	def ensure_dir(self, file_path):
		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			os.makedirs(directory)

	def BatchExtract(self, batch_num=1):
		print("Extracting batch", batch_num)
		image_list = []
		lower_bound = 0 + self.batch_size*(batch_num-1) 
		upper_bound = self.batch_size*batch_num
		for i in range(lower_bound, upper_bound):
			path = 'images/' + str(i+1) + '.jpg'			
			if not os.path.exists(path):				
				self.last_image = True
				return image_list
			image_list.append(path)
		return image_list
		
	def ExtractImageFeature(self, img_path, model):
	    img = image.load_img(img_path, target_size=(224, 224))
	    img_data = image.img_to_array(img)
	    img_data = np.expand_dims(img_data, axis=0)
	    img_data = preprocess_input(img_data)
	    vgg16_feature = model.predict(img_data)
	    return np.array(vgg16_feature).flatten()

	def Flatten(self, data):		
		result = []
		result.append(data[0])
		for i in data[1].tolist():
			result.append(i)	
		return result

	def SaveCSV(self, data, batch_num=1):
		with open('data.csv', 'a') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			for i in data:
				wr.writerow(self.Flatten(i))
		return

	def Extract(self):
		model = VGG16(weights='imagenet', include_top=False)
		i = 1	
		while(self.last_image != True):
			batch = self.BatchExtract(batch_num=i)
			data = []
			for path in batch:
				print(path)
				element = (path, self.ExtractImageFeature(path, model))	
				data.append(element)				
			#self.Save(data, i)
			self.SaveCSV(data, i)
			i += 1
		return