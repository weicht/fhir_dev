Purpose:
To test some FHIR REST APIs, explore DICOM Server capabilities, and tinker with Python.
Look at FHIR-DICOM.png to see the setup.

Status:
Very rough at the moment.  Mainly established connections with external systems by performing
basic Search queries.  Results are dumped to stdout and output flat files.  Want to:
- add a UI and deploy a Flask web server to make it more visual.
- add in some actual processing of the response vs just dumping it out.

Command Line:
fhir_dev.py is the main file that drives everything.



=====
References:

fhir-0.0.4 can be found here:
https://pypi.python.org/pypi/fhir

pydicom can be found here:
https://pypi.python.org/pypi/pydicom

Other tech details on pydicom may be found here:
https://code.google.com/p/pydicom/

DICOM files were obtained from:
http://www.osirix-viewer.com/datasets/

