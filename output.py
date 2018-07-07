import os
class Format():	
	def __init__(self):
		super(Format, self).__init__()
		print("Formatting output...")
		self.rename_folders()
	
	def rename_folders(self):
		path = os.path.join(os.getcwd(), "output/")		
		output_files = os.listdir(path)
		output_files = [float(x) for x in output_files]
		output_files.sort(reverse=True)
		for index, file_name in enumerate(output_files):
			folder = os.path.join(os.getcwd(), "output/"+str(file_name))
			renamed_folder = os.path.join(os.getcwd(), "output/"+str(index+1))
			os.rename(folder, renamed_folder)
		return 
		