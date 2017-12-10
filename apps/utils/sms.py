import logging
import random

import requests

from django.conf import settings

class Sms():
    verifycode_range = "1234567890"
    url = settings.SMS["url"]
    headers = {"Accept": "application/json",
    "charset": "utf-8"}
    logger = logging.getLogger(__name__)
    def generation_verifycode(self, length=4):
        return "".join(random.sample(Sms.verifycode_range, length))

    def send_verifycode(self, mobile):
        code = self.generation_verifycode()
        data = {
            "apikey": "947bfcde6345fa588917fedf930dae2c",
            "mobile": "18516770799",
            "text": "【天天生鲜】您的验证码是{}。如非本人操作，请忽略本短信".format(code)
        }
        try:
            # response = requests.post(self.url, data=data, timeout=5)
            # res = response.json()
            # if(res["code"] != 0):
            #     raise Exception(response.text)
            # self.logger.info(response.text)
            return code
        except Exception as exc:
            self.logger.error(exc)

        return None