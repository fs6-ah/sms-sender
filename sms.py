
import requests
Headers = {
    "Host": "rest.messagebird.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": "AccessKey مفتاح الحساب",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
    "Content-Type": "application/json",
    "Origin": "https://dashboard.messagebird.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://dashboard.messagebird.com/",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "85",
}
data = '{"body":"الرساله","originator":"اسم المرسل","recipients":"رقمك"}'
    

req = requests.post("https://rest.messagebird.com/messages", data=data, headers=Headers)
response = req.text
if req:
    print("[+]Done")
    print("--------------")
else:
    print("[+]FAILED")
    response
    print(response)
    print("--------------")
    exit()
response = req.text
print(response)
