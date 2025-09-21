from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def show_main(request):
    # Get filter parameter from the URL
    filter_param = request.GET.get('filter', None)
    
    # Filter items based on parameter
    if filter_param == 'my_items':
        # Show only the current user's items
        shop_list = Product.objects.filter(user=request.user)
    else:
        # Show all items
        shop_list = Product.objects.all()
    
    context = {
        'npm': '2406496422',
        'name': request.user.username,
        'class': 'PBP E',
        # Ubah product_list menjadi shop_list
        'shop_list': shop_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'page_title': 'Home - Football Shop',
        'current_year': datetime.now().year,
    }
    return render(request, "main.html", context)

def create_items(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        # Redirect ke halaman utama setelah berhasil membuat produk
        return redirect('main:show_main')

    context = {
        'form': form,
        'page_title': 'Create Product - Football Shop',
    }
    return render(request, "create_product.html", context)

def delete_item(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('main:show_main')

@login_required(login_url='/login')
def show_product(request, id):
    # Get the item by ID
    items = get_object_or_404(Product, pk=id)
    
    # Increment the view count field
    items.view_count += 1
    items.save(update_fields=['view_count'])  # Only save the view_count field
    
    context = {
        'items': items,
        'page_title': f'{items.name} - Football Shop',
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    items_list = Product.objects.all()
    xml_data = serializers.serialize("xml", items_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items_list = Product.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, item_id):
   try:
       item = Product.objects.filter(pk=item_id)
       xml_data = serializers.serialize("xml", item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, item_id):
   try:
       item = Product.objects.get(pk=item_id)
       json_data = serializers.serialize("json", [item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_shop(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "shop.html", context)