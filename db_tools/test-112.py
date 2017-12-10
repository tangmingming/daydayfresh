
import os
import sys
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, "{}/apps".format(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daydayfresh.settings")

import django

django.setup()

from goods.models import Classification, Merchandise, ShuffingFigure

from users.models import VerifyCode

querys = VerifyCode.objects.filter(send_time__gte=datetime.datetime.now()-datetime.timedelta(minutes=10))

print(querys)