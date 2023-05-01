from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import Sales

# Create your views here.

def index(request):
    sales_query = Sales.objects.values('product', 'price', 'purchase_date')

    total_sales_per_day = {}
    total_sales_per_product = {}
    for result in sales_query:
        product_name = result['product']
        day = result['purchase_date'].strftime('%a')

        # sales per product
        if total_sales_per_product.get(product_name):
            total_sales_per_product[product_name] += result['price']
        else:
            total_sales_per_product[product_name] = result['price']


        # sales per day
        if day in total_sales_per_day:
            total_sales_per_day[day] += result['price']
        else:
            total_sales_per_day[day] = result['price']

    # sales per product
    sales_product, labels_product = [], []
    for k, v in total_sales_per_product.items():
        sales_product.append(v)
        labels_product.append(k)


    # used for sorting days of the week
    key = {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thur': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
    }
    days = sorted(total_sales_per_day, key=key.get)
    sales_day, labels_day = [], []
    for k in days:
        sales_day.append(total_sales_per_day[k])
        labels_day.append(k)

    # Page from the theme 
    return render(request, 'pages/index.html', {
        'sales_product': sales_product, 'labels_product': labels_product,
        'sales_day': sales_day, 'labels_day': labels_day,
        })
