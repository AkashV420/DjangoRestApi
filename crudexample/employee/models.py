from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20, help_text='Unique Invoice ID for the particular entry')
    branch = models.CharField(max_length=5, default='Enter the branch(A, B or C)')
    city= models.CharField(max_length=20, default='Enter the name of city')
    customer_type = models.CharField(max_length=20,default='Normal or Member')
    gender = models.CharField(max_length=10,default='Male or Female')
    product_line = models.CharField(max_length=25,default='Enter the product line')
    unit_price = models.FloatField(default='enter unit price')
    quantity = models.CharField(max_length=20,default='1')
    tax = models.FloatField(default='tax')
    total = models.FloatField(default='enter total')
    payment_mode = models.CharField(max_length=10,default='Ewallet or Cash or Credit Card')
    rating = models.FloatField(max_length=4,default='0.0 to 10')
    class Meta:
        db_table = "employee"

class top_five(models.Model):#Class for Top 5 highly rated product line city wise
    rating = models.FloatField(max_length=4)
    product_line = models.CharField(max_length=25)
    city= models.CharField(max_length=20)

    def __str__(self):
        return self.product_line

class Total_amount(models.Model):#Class for Total Amount Payment mode wise
    total = models.FloatField(max_length=10)
    payment_mode = models.CharField(max_length=10)

    def __str__(self):
        return self.payment_mode

class Avg_product_rating(models.Model): #Class for Average Product Rating of Each Product line Branch wise
    rating = models.FloatField(max_length=4)
    product_line = models.CharField(max_length=25)
    branch = models.CharField(max_length=5)
    def __str__(self):
        return self.product_line
