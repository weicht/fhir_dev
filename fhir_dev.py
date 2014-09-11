#from __future__ import print_function
from fhir import *

# old .0.0.1 way
# rest = RestfulFHIR('http://fhir.healthintersections.com.au/open','Patient','name=Jimmy')

print '#### FHIR Search ####'
rest = RestfulFHIR('http://fhir.healthintersections.com.au/open', 'json')
#params = {'identifier': 55567890}
#params = {'gender:text': 'male'}
#params = {'gender:text': 'F', 'identifier': 55567890}
#params = {'subject._id': 55567890}


params = {'identifier': 444888888}
#params = {'given': 'Boris'}
query = rest.search('Patient', params)
print 'Query status: %s' % query

print 'Query response (query.text): '
print query.text
print '## End FHIR Search ####'

f1=open('./searchOutput.txt', 'w+')
print >>f1, repr(query.text)

#f2=open('./searchOuptputF2.txt', 'w+')
#t = u"%s", query.text
#print >> f2, t
print ''

print '#### FHIR Read ####'
rest = RestfulFHIR('http://fhir.healthintersections.com.au/open', 'json')
query = rest.read('Patient', 84239292)
print '[Good] Query status: '
print query
print '[Good] Query response (query.text): '
print query.text
print ''
query = rest.read('Patient', 84239292999)
print '[Bad] Query status: '
print query
print '[Bad] Query response (query.text): '
print query.text
print '## End FHIR Read ####'
