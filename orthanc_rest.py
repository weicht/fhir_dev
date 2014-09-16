import requests, json

_FILE_PATH = "./orthancOutput.txt"
_ORTHANC_HOST = "http://10.211.55.3"
_ORTHANC_PORT = "8042"
_ORTHANC_URL = _ORTHANC_HOST + ":" + _ORTHANC_PORT


def get_patient(patient_id):
	response = requests.get(_ORTHANC_URL +"/patients/"+patient_id)
	assert response.status_code == 200
	return response.text

def get_study(study_id):
	response = requests.get(_ORTHANC_URL +"/studies/"+study_id)
	assert response.status_code == 200
	return response.text

def get_series(series_id):
	response = requests.get(_ORTHANC_URL +"/series/"+series_id)
	assert response.status_code == 200
	return response.text

def get_instance(instance_id):
	response = requests.get(_ORTHANC_URL +"/instances/"+instance_id)
	assert response.status_code == 200
	return response.text


def Orthanc_Request():

	f = open(_FILE_PATH, 'w+')

	print '###################\n#### Orthanc Requests ####'
	response = requests.get(_ORTHANC_URL +"/patients")
	assert response.status_code == 200
	print "/patients\n" + response.text
	for patient in response.json():
		print "Patient: " + patient
	print >>f, "Patients:\n"+response.text

	response = requests.get(_ORTHANC_URL +"/studies")
	print "/studies\n" + response.text
	for study in response.json():
		print "Study: " + study
	print >>f, "Studies:\n"+response.text

	response = requests.get(_ORTHANC_URL +"/series")
	print "/series\n" + response.text
	for series in response.json():
		print "Series: " + series
	print >>f, "Series:\n"+response.text

	response = requests.get(_ORTHANC_URL +"/instances")
	print "/instances\n" + response.text
	for instance in response.json():
		print "Instance: " + instance
	print >>f, "Instances:\n"+response.text


	#Try to drill down a Patient->Studies->Series->Instances
	response = requests.get(_ORTHANC_URL +"/patients")
	assert response.status_code == 200
	patients = json.loads(response.text)
	for patient_id in patients:
		patient = json.loads(get_patient(patient_id))
		print "\n\nPatient:\n", json.dumps(patient)
		for study_id in patient["Studies"]:
#			print " "*4 + "Study ID: ", study_id
			study = json.loads(get_study(study_id))
			print " "*4 + "Study: "+study_id+"\n" + " "*4 + json.dumps(study)
			for series_id in study["Series"]:
#				print " "*8 + "Series ID: ", series_id
				series = json.loads(get_series(series_id))
				print " "*8 + "Series: "+series_id+"\n" + " "*8 + json.dumps(series)
				for instance_id in series["Instances"]:
#					print " "*12 + "Instance ID: ", instance_id
					instance = json.loads(get_instance(instance_id))
					print " "*12 + "Instance: "+instance_id+"\n" + " "*12 + json.dumps(instance)

	print '## End Orthanc Requests ####'
