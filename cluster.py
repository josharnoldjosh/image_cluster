# Load arguments
import argparse, sys, os
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--group", required=False, help="The number of images to group and eventually cluster. Default is to cluster all images in the directory.", type=int, const=sys.maxsize, nargs='?')
ap.add_argument("-i", "--imageset", required=False, help="The number of images per image set. An integer value.", type=int, const=20, nargs='?')
ap.add_argument("-s", "--scratch", required=False, help="Should we cluster all images from scratch?", type=str2bool, const=False, nargs='?')
args = vars(ap.parse_args())

# Delete files to recluster if necessary
import shutil
if args["scratch"] == True:	
	try:
		os.remove('data.csv')
		os.remove('matrix.csv')
	except OSError:
		pass
	shutil.rmtree('images', ignore_errors=True)
	shutil.rmtree('output', ignore_errors=True)
	shutil.rmtree('__pycache__', ignore_errors=True)	

import group, extract, matrix, create, output

# Group images
group.GroupImages(limit=args["group"])

# Batch extract their image features
extract.ExtractImageFeatures(batch_size=5000)

# Dot matrix
matrix.Dot()

# Create image sets
create.CreateImageSets(i = args["imageset"])

# Format output
output.Format()

print("Script done.")
