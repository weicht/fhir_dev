from fhir import *
import dicom
from PIL import Image


def DCM_Parsing():
	_FILE_PATH = "./dicomOutput.txt"
	_INPUT_FILE = "./dicom_files/IM-0001-0082.dcm"

	print '###################\n#### DCM File Parsing ####'
	ds = dicom.read_file(_INPUT_FILE)
	# Reference this page to see what fields are available by Tag Name:
	#  http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/DICOM.html
	print "Patient.Name: %s " % ds.PatientName
	print ds
#	im = Image.fromarray(ds.pixel_array)
#	im.show()

	print >>open(_FILE_PATH, 'w+'), ds
	print '## End DCM File Parsing ####'
