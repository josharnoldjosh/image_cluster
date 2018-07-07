import os
import pandas as pd
import numpy as np
from shutil import copyfile
import shutil

class CreateImageSets():	
	def __init__(self, i = 40):
		super(CreateImageSets, self).__init__()		
		shutil.rmtree('output/', ignore_errors=True)
		self.CreateImageSets(i)		

	def LargestIndicies(self, ary, n):		
		flat = ary.flatten()
		indices = np.argpartition(flat, -n)[-n:]
		indices = indices[np.argsort(-flat[indices])]
		return np.unravel_index(indices, ary.shape)[0].tolist()

	def ensure_dir(self, file_path):
		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			os.makedirs(directory)

	def GetSimValue(self, row, best):
		s = 0
		for i in best:
			s += row[i]
		return s		

	def CopyImage(self, i, j, k):		
		img_name = str(j) + '.jpg'
		path_orig = os.path.join(os.getcwd(), 'images/'+img_name)
		dst = os.path.join(os.getcwd(), 'output/'+str(i)+'/')
		self.ensure_dir(dst)
		copyfile(path_orig, os.path.join(dst, str(k)+'.jpg'))
		return
		
	def CreateImageSets(self, num_sets = 20):
		print("Reloading matrix...")
		df = pd.read_csv('matrix.csv', header=None)				

		print("Creating image sets...")
		for index, row in df.iterrows():
			best = self.LargestIndicies(row.values, num_sets+1)
			best.pop(0)
			sim = self.GetSimValue(row, best)
			for i, j in enumerate(best):				
				self.CopyImage(sim, j, i+1)	
		return
