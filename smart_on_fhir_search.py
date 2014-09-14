from fhir import *
import feedparser


def SMART_On_FHIR_Search():
	_FILE_PATH = "./smartOnFhirSearchOutput.txt"

	print '#### SMART On FHIR Search ####'
	rest = RestfulFHIR('http://fhir-open-api.smartplatforms.org', 'xml')
	params = {'accession': '87654321'}
#	params = {}

#https://fhir-open-api.smartplatforms.org/ImagingStudy?series=urn:sampleoid:2.16.124.113543.6003.sample.2.3
#https://fhir-open-api.smartplatforms.org/ImagingStudy?accession=87654321

	query = rest.search('ImagingStudy', params)
#	query = rest.read('ImagingStudy', '')
	print 'Query status: %s' % query
	# Parse the response Atom xml
	d = feedparser.parse(query.text)
	print len(d['entries'])
	for post in d.entries:
	    print post.title + " // " + post.id

	print >>open(_FILE_PATH, 'w+'), repr(query.text)
	print ''

	print '## End SMART On FHIR Search ####'
