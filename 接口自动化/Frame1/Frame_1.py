__author__ = 'Administrator'
from Frame1.HttpRequest import HttpRequest

path = "http.conf"

reg = HttpRequest(path)

#reg.get_req()
reg.post_req()