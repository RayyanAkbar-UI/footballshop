from django.urls import path
from main.views import create_items, show_main, show_shop, show_xml, show_json, show_json_by_id, show_xml_by_id, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('items/create/', create_items, name='create_items'),
    path('items/<int:id>/', show_shop, name='show_shop'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('items/<int:id>/delete/', delete_item, name='delete_item'), #test
]