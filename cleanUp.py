import os, glob, sys
images = glob.glob("*.jpg")
if(len(images) < 0):
	sys.exit(0)
else:
	num = len(images)
	print("Detected " + str(num) + " image files.")
	for i in images:
		os.remove(i)
	print("Deleted " + str(num) + " images.")
