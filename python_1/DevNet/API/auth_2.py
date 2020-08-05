import requests


url = "https://postman-echo.com"

payload = {}
headers= {}



payload = {}
headers = {"Authorization": "Basic cG9zdG1hbjpwYXNzd29yZA==",
"Cookie":'sails.sid=s%3AL0ZlpBwhiSARx55dDvUtlftzdPV3eEom.QCXBkpiCnWfy%2BQLY55WnEDmLPniW1ZHkG8C9WiVo1Ts'

}

get = requests.get(url, headers=headers, data=payload)



print(get)