
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, "{}/apps".format(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daydayfresh.settings")

import django

django.setup()


from goods.models import Merchandise, ShuffingFigure, Classification

from db_tools.data.product_data import row_data

# subclass = models.ForeignKey("Classification", verbose_name="所属分类")
# front_cover_img = models.ImageField(upload_to="", verbose_name="商品封面图")
# sn = models.CharField(max_length=50, unique=True, verbose_name="编号")
# name = models.CharField(max_length=30, verbose_name="商品名称")
# desc = models.CharField(max_length=100, verbose_name="商品描述")
# prise = models.FloatField(verbose_name="价格")
# particulars = UEditorField(imagePath="goods/images", width=1000, height=300, filePath="goods/files/", default="",
#                            verbose_name="商品详情")
# activity_prise = models.FloatField(null=True, blank=True, verbose_name="活动价格")
# lower_time = models.DateTimeField(null=True, blank=True, verbose_name="下架时间")
# inventory_num = models.IntegerField(default=0, verbose_name="库存")
# click_num = models.IntegerField(default=0, verbose_name="点击数")
# sales_numm = models.IntegerField(default=0, verbose_name="销售量")
# is_new = models.BooleanField(default=False, verbose_name="是否为新品")
# is_hot = models.BooleanField(default=False, verbose_name="是否为热卖")
# add_time = models.DateTimeField(default=datetime.now, verbose_name="上架时间")

count = 0

for i in row_data:
    count += 1
    mer = Merchandise()
    front_cover_img = ""
    try:
        front_cover_img = i["images"][0]
    except:
        pass


    mer.subclass = Classification.objects.filter(name=i["categorys"][-1])[0]
    mer.front_cover_img = front_cover_img
    mer.sn = str(count)
    mer.name = i["name"]
    mer.desc = i["desc"]
    mer.particulars = i["goods_desc"]
    mer.market_price = float(i["market_price"].replace("￥", "").replace("元", ""))
    mer.sale_price = float(i["sale_price"].replace("￥", "").replace("元", ""))

    mer.save()
    print(mer)
    for j in range(len(i["images"])):
        shu = ShuffingFigure()
        shu.merchandise = mer
        shu.img = i["images"][j]
        shu.index = j
        shu.save()