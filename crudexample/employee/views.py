from django.http import JsonResponse
from rest_framework import viewsets
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import top_five
from .models import Avg_product_rating
from .models import Total_amount
from .serializers import Avg_product_ratingSerializer
from .serializers import top_fiveSerializer
from .serializers import Total_amountSerializer

from django.db.models import Sum
from django.db.models import Avg

class Avg_product_ratingList(APIView):#Average Product Rating of Each Product line Branch wise
    def get(self, request):
        avgpr = Avg_product_rating.objects.order_by('branch ')
        serializer = Avg_product_ratingSerializer(avgpr, many=True)
        return  Response(serializer.data)
    def post(self):
        pass
class top_fiveList(APIView):#Top 5 highly rated product line city wise
    def get(self, request):
        topf = top_five.objects.order_by('city')
        serializer = top_fiveSerializer(topf, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Total_amountList(APIView):# Total Amount Payment mode wise
    def get(self, request):
        totala = Total_amount.objects.order_by('payment_mode')
        serializer = Total_amountSerializer(totala, many=True)
        return Response(serializer.data)
    def post(self):
        pass

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
