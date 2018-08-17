import requests
import json
data = {
    "user_key":"PIgPamw733rw",
    "type":"text",
    "content":"\xec\x95\x88\xeb\x85\x95"
}

url ='http://6ce34d64.ap.ngrok.io/message'
headers ={
'X-Forwarded-For':'110.76.143.234',
'Content-Type': 'application/json; charset=utf-8',
'Content-Length': '60',
'Host': '6ce34d64.ap.ngrok.io',
'Accept': '*/*',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
'Via': '1.1 ghost377 (squid/3.1.23)',
'Cache-Control': 'max-age=259200',


}

requests.post(url,data=json.dumps(data), headers=headers)
