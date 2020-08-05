from ncclient import manager

equipo = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
 "username": "developer", "password": "C1sco12345" }



with manager.connect(host=equipo["host"], port=equipo["port"], username=equipo["username"], password=equipo["password"], hostkey_verify=False) as m:
    m.close_session()

