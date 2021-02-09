import requests
import sys
import json

f = open('data.json', "r")
data = json.load(f)

class Librus:
    host = "https://api.librus.pl/"
    headers = {
        "Authorization": "Basic Mjg6ODRmZGQzYTg3YjAzZDNlYTZmZmU3NzdiNThiMzMyYjE="
    }

    r = requests.post(host + "OAuth/Token", data={"username": data['login'],
                                                       "password": data['password'],
                                                       "librus_long_term_token": "1",
                                                       "grant_type": "password"}, headers= headers)
    headers["Authorization"] = "Bearer " + r.json()["access_token"]
    ln = requests.get(host + "2.0/" + "Grades", headers=headers)
    #print((ln).text)`
    #lucky_number = ln.json()
    print((ln).text)
    subjects = {i["Id"]: i["Name"] for i in ln.json()["Subjects"]}
    print(subjects)
    print(lucky_number)





"""
import requests
import os
import json
#########
def luckyNumber():
    luckyNumber_int = home.find("luckyNumber")
    luckyNumber = (home[luckyNumber_int + 22] + home[luckyNumber_int + 23])
    print(luckyNumber)
#########
host = 'http://api.librus.pl'
f = open('data.json', "r")
data = json.load(f)
login = data['login']
password = data['password']
lucky_number = None
r = requests.session()
r.get('https://api.librus.pl/OAuth/Authorization?client_id=46&response_type=code&scope=mydata')
r.post("https://api.librus.pl/OAuth/Authorization/Grant?client_id=46", data={
    'grant_type': 'password',
    'username': login,
    'password': password,
    'librus_long_term_token': '1'})
r.get('https://api.librus.pl/OAuth/Authorization/Grant?client_id=46')
home = r.get("https://synergia.librus.pl/uczen/index")
grades = r.get("https://synergia.librus.pl/przegladaj_oceny/uczen")
print(r.get('https://api.librus.pl/2.0/SchoolNotices').text)

#luckyNumber()

"""