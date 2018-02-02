from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Classification(models.Model):
    """
    商品分类
    """
    C_TYPE = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
    )

    parent_class = models.ForeignKey("self", related_name="childs", null=True, blank=True, verbose_name="父分类")
    name = models.CharField(max_length=30, verbose_name="分类名称")
    code = models.CharField(max_length=30, verbose_name="唯一编码")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="描述")
    c_type = models.SmallIntegerField(choices=C_TYPE, verbose_name="分类级别")
    is_show_navi = models.BooleanField(default=False, verbose_name="是否显示再导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类-plu"

    def __str__(self):
        return self.name

class ClassImg(models.Model):
    classification = models.ForeignKey("Classification", verbose_name="所属分类")
    name = models.CharField(max_length=30, default="", blank=True, verbose_name="图片名称")
    img = models.ImageField(verbose_name="图片")

    class Meta:
        verbose_name = "分类图片"
        verbose_name_plural = "分类图片-plu"

    def __str__(self):
        return self.name

class Merchandise(models.Model):
    """
    商品
    """
    subclass = models.ForeignKey("Classification", verbose_name="所属分类")
    front_cover_img = models.ImageField(upload_to="", verbose_name="商品封面图")
    sn = models.CharField(max_length=50, unique=True, verbose_name="编号")
    name = models.CharField(max_length=30, verbose_name="商品名称")
    desc = models.TextField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    market_price = models.FloatField(verbose_name="价格")
    sale_price = models.FloatField(null=True, blank=True, verbose_name="活动价格")
    particulars = UEditorField(imagePath="goods/images", width=1000, height=300, filePath="goods/files/", default="", verbose_name="商品详情")
    lower_time = models.DateTimeField(null=True, blank=True, verbose_name="下架时间")
    inventory_num = models.IntegerField(default=0, verbose_name="库存")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sales_numm = models.IntegerField(default=0, verbose_name="销售量")
    is_new = models.BooleanField(default=False, verbose_name="是否为新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否为热卖")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="上架时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ShuffingFigure(models.Model):
    """
    商品轮播图
    """
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")
    name = models.CharField(max_length=30, default="", blank=True, verbose_name="图片名称")
    img = models.ImageField(verbose_name="商品图片")
    index = models.SmallIntegerField(default=0, verbose_name="图片位置")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexShuffingFigure(models.Model):
    """
    主页轮播图
    """
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")
    name = models.CharField(max_length=30, default="", blank=True, verbose_name="图片名称")
    img = models.ImageField(verbose_name="商品图片")
    index = models.SmallIntegerField(default=0, verbose_name="图片位置")
