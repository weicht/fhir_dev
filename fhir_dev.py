#from __future__ import print_function
from fhir import *
from lxml import objectify, etree
import feedparser
from fhir_search import *
from fhir_read import *
from bad_request import *
from fhir_dicom_search import *


#Do a FHIR Search
FHIR_Search()

#Do a FHIR DICOM Read
FHIR_Read()

#Operation Outcome set with 404 for a bad request
FHIR_Bad_Request()

#Perform some Search/Read requsts agains the FHIR-DICOM server
FHIR_DICOM_Search()
