import pandas as pd
import os


class Dot(object):	
	def __init__(self):
		super(Dot, self).__init__()
		if (self.PathExists('matrix.csv')):
			return
		else:
			self.Dot()

	def PathExists(self, path):
		full_path = os.path.join(os.getcwd(), path)
		if os.path.exists(full_path):
			return True
		return False

	def Dot(self):
		print("Loading extracted image features...")
		df = pd.read_csv('data.csv', header=None)
		df = df.drop(df.columns[0], axis=1)				

		print("Creating transpose...")
		df_T = df.transpose()		

		print("Performing dot product...")
		df_dot = df.dot(df_T)				

		print("Saving matrix...")
		df_dot.to_csv('matrix.csv', header=None)		
		return

