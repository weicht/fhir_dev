from fhir import *


def FHIR_Bad_Request():
	_FILE_PATH = "./badOutput.txt"

	print '##########################\n#### FHIR Bad Request ####'
	rest = RestfulFHIR('http://fhir.healthintersections.com.au/open', 'json')
	#testing a bad request - Patient does NOT exist
	query = rest.read('Patient', 84239292999)
	print >>open(_FILE_PATH, 'w+'), repr(query.text)
	print query.text
	print '## End FHIR Bad Request ####'

