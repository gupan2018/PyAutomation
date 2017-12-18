__author__ = 'Administrator'
from suds.client import Client


url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
client = Client(url)
#print(client) #打印接口信息，包括这个接口下有哪些方法

data = {
    "client_ip":"129.23.10.2",
    "mobile":"13896082955",
    "tmpl_id":"1"
}
res = client.service.sendMCode(data)
print(res)