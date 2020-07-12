from rest_framework import serializers
from .models import Avg_product_rating
from .models import top_five
from .models import Total_amount

class Avg_product_ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avg_product_rating
        fields = '__all__'

class top_fiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = top_five
        fields = '__all__'

class Total_amountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_amount
        fields = '__all__'
