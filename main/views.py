from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags

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
            
            response = HttpResponseRedirect(reverse('main:show_main'))
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

@login_required(login_url='/login/')
def show_main(request):
    filter_param = request.GET.get('filter', None)
    category_filter = request.GET.get('category')
    
    if filter_param == 'my_items'and request.user.is_authenticated:  
        shop_list = Product.objects.filter(user=request.user)
    else:
        shop_list = Product.objects.all()
    
    if category_filter:
        shop_list = shop_list.filter(category=category_filter)

    categories = Product.CATEGORY_CHOICES
    

    context = {
        'npm': '2406496422',
        'name': request.user.username,
        'class': 'PBP E',
        'shop_list': shop_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'page_title': 'Home - Football Shop',
        'current_year': datetime.now().year,
        'product_categories': categories,
    }
    return render(request, "main.html", context)

def create_items(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

@login_required(login_url='/login/')
def show_product(request, id):
    items = get_object_or_404(Product, pk=id)
    
    items.view_count += 1
    items.save(update_fields=['view_count'])  
    
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
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'formatted_price': product.formatted_price(),
            'description': product.description,
            'quantity': product.quantity,
            'category': product.category,
            'image': product.image.url if product.image else None,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'view_count': product.view_count,
            'user_id': product.user.id,
            'username': product.user.username,
        })
    return JsonResponse(data, safe=False)

def get_product_json(request, id):
    product = get_object_or_404(Product, id=id)
    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'formatted_price': product.formatted_price(),
        'description': product.description,
        'quantity': product.quantity,
        'category': product.category,
        'image': product.image.url if product.image else None,
        'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'view_count': product.view_count,
        'user_id': product.user.id,
        'username': product.user.username,
    }
    return JsonResponse(data)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = strip_tags(request.POST.get('name'))
        price = request.POST.get('price')
        description = strip_tags(request.POST.get('description'))
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.POST.get('image')
        
        import re
        price = re.sub(r'[^\d]', '', price) if price else 0
        
        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            quantity=quantity,
            category=category,
            user=request.user
        )
        
        return JsonResponse({
            "status": True,
            "message": "Product created successfully!",
            "product_id": product.id
        }, status=201)
    
    return JsonResponse({"status": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def update_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        
        product.name = strip_tags(request.POST.get('name'))
        
        price = request.POST.get('price')
        import re
        product.price = re.sub(r'[^\d]', '', price) if price else 0
        
        product.description = strip_tags(request.POST.get('description'))
        product.quantity = request.POST.get('quantity')
        product.category = request.POST.get('category')
        
        image = request.POST.get('image')
        if image:
            product.image = image
            
        product.save()
        
        return JsonResponse({
            "status": True,
            "message": "Product updated successfully!"
        }, status=200)
    
    return JsonResponse({"status": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.delete()
        
        return JsonResponse({
            "status": True,
            "message": "Product deleted successfully!"
        }, status=200)
    
    return JsonResponse({"status": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            response = JsonResponse({
                "status": True,
                "message": "Login successful!",
                "username": user.username
            })
            response.set_cookie('last_login', str(datetime.now()))
            return response
        else:
            return JsonResponse({
                "status": False,
                "message": "Invalid username or password."
            }, status=401)
    
    return JsonResponse({"status": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if not username or not password1 or not password2:
            return JsonResponse({
                "status": False, 
                "message": "Please fill all required fields."
            }, status=400)
            
        if password1 != password2:
            return JsonResponse({
                "status": False, 
                "message": "Passwords don't match."
            }, status=400)
        
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False, 
                "message": "Username already taken."
            }, status=400)
            
        user = User.objects.create_user(username=username, password=password1)
        
        return JsonResponse({
            "status": True,
            "message": "Registration successful! Please login.",
            "username": user.username
        }, status=201)
    
    return JsonResponse({"status": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def logout_ajax(request):
    logout(request)
    response = JsonResponse({
        "status": True,
        "message": "Logged out successfully!"
    })
    response.delete_cookie('last_login')
    return response

def show_navbar(request):
    """
    View function to display the simple navbar template
    """
    categories = Product.CATEGORY_CHOICES
    context = {
        'product_categories': categories,
        'page_title': 'Navigation Bar Example'
    }
    return render(request, "simple_navbar.html", context)

def show_xml_by_id(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    xml_data = serializers.serialize("xml", [item])
    return HttpResponse(xml_data, content_type="application/xml")

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if user is authorized to edit this product
    if product.user != request.user:
        messages.error(request, "You don't have permission to edit this product.")
        return redirect('main:show_main')
        
    # Process the form
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('main:show_product', id=product.id)
    else:
        form = ProductForm(instance=product)
        
    context = {
        'form': form,
        'product': product,
        'page_title': f'Edit {product.name} - Football Shop',
    }
    return render(request, "edit_product.html", context)