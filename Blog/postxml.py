__author__ = 'shety'
import urllib2
import sys
import httplib

def SendRtx(jobmame,reponame):

    str1 = \
            '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://www.businessobjects.com/DataServices/ServerX.xsd"><soapenv:Body><ser:RunBatchJobRequest><jobName>'''
    str2 = \
        '''</jobName><repoName>'''
    str3 = \
        '''</repoName></ser:RunBatchJobRequest></soapenv:Body></soapenv:Envelope>'''

    SENDTPL = str1 + jobmame + str2 + reponame +str3
    SoapMessage = SENDTPL
    webservice = httplib.HTTP("172.16.100.33")
    webservice.putrequest("POST", "http://sapds.ciicsh.local/DataServices/servlet/webservices?ver=2.1")
    webservice.putheader("Host", "172.16.100.33")
    webservice.putheader("User-Agent", "Python Post")
    webservice.putheader("Content-type", "text/xml")
    webservice.putheader("Content-length", "%d" % len(SoapMessage))
    webservice.putheader("SOAPAction", "jobAdmin=Run_Batch_Job")
    webservice.endheaders()
    webservice.send(SoapMessage)
    # get the response
    statuscode, statusmessage, header = webservice.getreply()
    print "Response: ", statuscode, statusmessage
    print "headers: ", header
    print webservice.getfile().read()
    return 0;