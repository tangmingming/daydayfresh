
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, "{}/apps".format(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daydayfresh.settings")

import django

django.setup()

from goods.models import Classification, Merchandise, ShuffingFigure

from db_tools.data.category_data import row_data

# for i in row_data:
#     c_1 = Classification(name=i["name"], code=i["code"])
#     c_1.save()
#     for j in i["sub_categorys"]:
#         c_2 = Classification(parent_class=c_1, name=j["name"], code=j["code"])
#         c_2.save()
#         for k in j["sub_categorys"]:
#             c_3 = Classification(parent_class=c_2, name=k["name"], code=k["code"])
#             c_3.save()


# c = Classification(name="test-111", code="123333")
# b = c.save()
# print(b)
#
o = Merchandise.objects.all()
for i in o:
    i.delete()

o = ShuffingFigure.objects.all()
for i in o:
    i.delete()



        # jxmc = Merchandise.objects.get(name="精选茗茶")
#
# print(jxmc.__dict__)