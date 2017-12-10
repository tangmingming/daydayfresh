import json

import requests

url = "https://sms.yunpian.com/v2/sms/single_send.json"
headers = {
    "Accept": "application/json",
    "charset": "utf-8"
}
data = {
	"apikey":"947bfcde6345fa588917fedf930dae2c",
	"mobile":"18516770799",
	"text":"【天天生鲜】您的验证码是1234。如非本人操作，请忽略本短信"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)