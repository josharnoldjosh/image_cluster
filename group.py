import os, shutil, sys

class GroupImages:	
	def __init__(self, limit=sys.maxsize):
		super(GroupImages, self).__init__()
		self.GroupImages(limit=limit)		

	def PathExists(self, path):
		full_path = os.path.join(os.getcwd(), path)
		if os.path.exists(full_path):
			return True
		return False

	def GroupImages(self, limit=sys.maxsize):
		if self.PathExists('images'):
			return
		print("Finding images...")
		files = [os.path.join(root, name)
	             for root, dirs, files in os.walk(os.getcwd())
	             for name in files
	             if name.endswith((".png", ".jpg"))]
		output_dir = os.path.join(os.getcwd(), 'images')
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)		
		print("Grouping images...")
		i = 1
		for file in files:
			output_file_name = str(i) + '.jpg'
			shutil.copy(file, os.path.join(output_dir, output_file_name))
			i += 1
			if (i > limit):
				break		
		print(i-1, "images grouped.")
