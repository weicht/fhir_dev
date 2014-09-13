from fhir import *
import feedparser


def FHIR_DICOM_Search():
	_FILE_PATH = "./dcomSearchOutput.txt"

	print '#### FHIR-DICOM Search ####'
	# Look here for all the Params avail for Patient and ImagingStudy
	#  - http://fhir.dicomserver.co.uk/
	# Note: The server this is going against is Under Development
	rest = RestfulFHIR('http://fhir.dicomserver.co.uk/', 'xml')
	params = {'gender': 'F'}
	query = rest.search('Patient', params)
	print 'Query status: %s' % query
	# Parse the response Atom xml
	d = feedparser.parse(query.text)
	print len(d['entries'])
	for post in d.entries:
	    print post.title + " // " + post.id + "\n"

	print >>open('./dcomQueryOutput.txt', 'w+'), repr(query.text)
	print ''

	print '## End FHIR-DICOM Search ####'
