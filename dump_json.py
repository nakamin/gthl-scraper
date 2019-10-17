import requests
from pyquery import PyQuery as pq

url = "https://ssp.agilex.ca/gthlssp/standings.aspx"

headers_1 = {
    "Referer": "https://www.gthlcanada.com/leaguestandings/",
    "Cookie": "AGILEX=Division=MBN&Category=A1&Season=19-20&Region=East",
}

response = requests.request("GET", url, headers=headers_1)

d = pq(response.text)
vs = d("#__VIEWSTATE")
ev = d("#__EVENTVALIDATION")

payload = {
    "__EVENTVALIDATION": ev,
    "__VIEWSTATE": vs,
    "__VIEWSTATEENCRYPTED": "",
    "ddlCat": "A1",
    "ddlDiv": "MBN",
    "ddlRegion": "East",
    "ddlSeason": "19-20",
}

formdata = urllib.parse.urlencode(payload)

alexteams = requests.request("POST", url, data=payload)

print("st_RepeaterBody" in alexteams.text)
