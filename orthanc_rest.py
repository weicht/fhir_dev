import requests

def Orthanc_Request():
	_FILE_PATH = "./orthancOutput.txt"
	_ORTHANC_HOST = "http://10.211.55.3"
	_ORTHANC_PORT = "8042"
	_ORTHANC_URL = _ORTHANC_HOST + ":" + _ORTHANC_PORT

	print '###################\n#### Orthanc Requests ####'
	response = requests.get(_ORTHANC_URL +"/patients")
	assert response.status_code == 200
	print "/patients\n" + response.text
	for patient in response.json():
		print "Patient: " + patient

	print "/studies\n" + response.text
	for study in response.json():
		print "Study: " + study

	print "/series\n" + response.text
	for series in response.json():
		print "Series: " + series

	print "/instances\n" + response.text
	for instance in response.json():
		print "Instance: " + instance

#http://10.211.55.3:8042/patients/63ad0782-df664bdf-d844f071-e6d2f979-14ecf504



	print '## End Orthanc Requests ####'
