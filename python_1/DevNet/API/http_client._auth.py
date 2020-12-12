import http.client
import mimetypes
import requests

from requests.api import request


#url = "https://postman-echo.com"
page = http.client.HTTPSConnection("postman-echo.com")
payload = ''
headers = {
  'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA==',
  'Cookie': 'sails.sid=s%3AL0ZlpBwhiSARx55dDvUtlftzdPV3eEom.QCXBkpiCnWfy%2BQLY55WnEDmLPniW1ZHkG8C9WiVo1Ts'
}

page.request("GET", "/basic-auth", payload, headers)
res = page.getresponse()
data = res.read()

#conexion = requests.get(url ,  headers=headers, data=payload)

print(data.decode("utf-8"))
#print(conexion.text.encode("utf-8"))