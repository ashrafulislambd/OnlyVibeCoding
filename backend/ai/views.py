from django.shortcuts import render
from product.extentions import get_all_products_summary

def index(request):
    summary = get_all_products_summary()
    return render(request, "ai/index.html", {"summary" : summary})
