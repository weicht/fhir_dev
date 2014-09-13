from fhir import *


def FHIR_Read():
	_FILE_PATH = "./readOutput.txt"

	print '###################\n#### FHIR Read ####'
	rest = RestfulFHIR('http://fhir.healthintersections.com.au/open', 'json')
	query = rest.read('Patient', 102)
	print >>open(_FILE_PATH, 'w+'), repr(query.text)
	# print '[Good] Query status: '
	# print query
	# print '[Good] Query response (query.text): '
	print query.text
	print '## End FHIR Read ####'
