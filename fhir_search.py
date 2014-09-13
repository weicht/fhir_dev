from fhir import *
#from lxml import objectify, etree
import feedparser


def FHIR_Search():
	_FILE_PATH = "./searchOutput.txt"

	print '#### FHIR Search ####'
	# Look here for all the Search Params avail for Patient
	#  - http://fhir.healthintersections.com.au/open/Patient
	# Note: The API groups the results into groups of 50 UNLESS
	#  you set the _count parameter to something high
	rest = RestfulFHIR('http://fhir.healthintersections.com.au/open', 'xml')

	#params = {'identifier': 55567890}
	#params = {'gender:text': 'F', 'identifier': 55567890}
	#params = {'subject._id': 55567890}
	#params = {'gender:text': 'M'}
	#params = {'identifier': 444888888}
	#params = {'given': 'Boris'}
	#params = {'gender': 'F', '_count': 1000}
	params = {'gender': 'F'}
	query = rest.search('Patient', params)
	print >>open(_FILE_PATH, 'w+'), repr(query.text)
	#print 'Query status: %s' % query
	#print 'Query response (query.text): '
	#print query.text

	# Parse the response Atom xml
	d = feedparser.parse(query.text)
	print len(d['entries'])
	for post in d.entries:
	    print post.title + " // " + post.id
	print '## End FHIR Search ####'

