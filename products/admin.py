from django.contrib import admin
from products import models as pm

admin.site.register(pm.Category)
admin.site.register(pm.SubCategory)
admin.site.register(pm.Product)
