from WebDriver_Soap.Http_Soap_Class import HttpGet
from WebDriver_Soap.Http_Soap_Class import HttpPost
from WebDriver_Soap.Http_Soap_Class import Soap

path = "C:\\Users\\Administrator\\PycharmProjects\\test\\hk0607.conf"

GetTest = HttpGet(path)
PostTest = HttpPost(path)
SoapTest = Soap(path)

GetTest.Req()
PostTest.Req()
SoapTest.Req()
