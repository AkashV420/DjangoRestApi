from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('',views.show),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    url(r'^AverageProductRating/',views.Avg_product_ratingList.as_view()),# Average Product Rating of Each Product line Branch wise
    url(r'^topfive/',views.top_fiveList.as_view()),#Top 5 highly rated product line city wise
    url(r'^Totalamount/',views.Total_amountList.as_view()),# Total Amount Payment mode wise
]
