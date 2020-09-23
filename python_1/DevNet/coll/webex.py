import requests
import json

token = "ZDQ2NGVjZTktMWRjOC00Y2Q2LWI5MDAtNTFlNDRjYTg4ZGNlMDgwZmY5MzEtYmI3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

url_teams = "https://webexapis.com/v1/teams"

headers = {"Authorization" : f"Bearer {token}",
            "Content-Type":"application/json" }

body = {"name": "python_webex"} #data se debe de enviar en json#
#post = requests.post(url_teams, headers=headers, data=json.dumps(body)).json()#crear teams####

get = requests.get(url_teams, headers=headers).json()
#print(get)
#temasId = get["items"][0]["id"]
#print(temasId)
teams = get["items"]
for team in teams:
    if team["name"]== 'python_webex':
        teamId = team["id"] 
        print(teamId)

# ######## crear rooms ####
# url_room = "https://webexapis.com/v1/rooms"

# room_body = {"title":"python_room_teams",
#          "teamId" : teamId }

# # post_room = requests.post(url_room, headers=headers, data=json.dumps(room_body)).json() 

# get_rooms = requests.get(url_room, headers=headers).json()
# print(json.dumps(get_rooms, indent=2, sort_keys=True))
# rooms = get_rooms["items"]
# for room in rooms:
#     if room["title"]=="python_room_teams":
#         roomId = room["id"]
#         print(roomId)

# ##### message room ####

# message_url = "https://webexapis.com/v1/messages"

# message_body = {"roomId": roomId,
#             "text":"Hola Lili"}

# post_message = requests.post(message_url, data=json.dumps(message_body), headers=headers)
# #print(post_message.ok)
# # if post_message.ok == True:
# #     print("ok")
# print(post_message.status_code)

messageId = "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjJjMTE5OTAtZmQ0ZC0xMWVhLTk3ZjAtN2JhMGU1YjYwZjFh"

url_delete = "https://webexapis.com/v1/messages/" + messageId

delete = requests.delete(url_delete, headers=headers)
print(delete)























