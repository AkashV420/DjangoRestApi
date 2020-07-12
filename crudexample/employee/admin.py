from django.contrib import admin
from . models import top_five
from . models import Total_amount
from . models import Avg_product_rating

admin.site.register(top_five)
admin.site.register(Total_amount)
admin.site.register(Avg_product_rating)
