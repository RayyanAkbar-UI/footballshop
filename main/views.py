from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm
from main.models import Shop
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    shop_list = Shop.objects.all()

    context = {
        'npm' : '2406496422',
        'name': 'Rayyan Akbar Gumilang',
        'class': 'PBP E',
        'shop_list': shop_list
    }

    return render(request, "main.html", context)

def create_items(request):
    form = ShopForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)

def delete_item(request, id):
    shop = get_object_or_404(Shop, id=id)
    shop.delete()
    return redirect('main:show_main')

def show_shop(request, id):
    shop = get_object_or_404(Shop, pk=id)

    context = {
        'shop': shop
    }

    return render(request, "shop_detail.html", context)

def show_xml(request):
    items_list = Shop.objects.all()
    xml_data = serializers.serialize("xml", items_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items_list = Shop.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, item_id):
   try:
       item = Shop.objects.filter(pk=item_id)
       xml_data = serializers.serialize("xml", item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, item_id):
   try:
       item = Shop.objects.get(pk=item_id)
       json_data = serializers.serialize("json", [item])
       return HttpResponse(json_data, content_type="application/json")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)