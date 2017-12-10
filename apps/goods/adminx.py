import xadmin

from . import models

class MerchandiseAdmin:
    # list_display = ("name", "desc", "add_time")
    pass

class ClassificationAdmin:
    pass


xadmin.site.register(models.Classification, ClassificationAdmin)
xadmin.site.register(models.Merchandise, MerchandiseAdmin)
xadmin.site.register(models.ShuffingFigure)
xadmin.site.register(models.IndexShuffingFigure)
