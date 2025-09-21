from django.urls import path
from main.views import create_items, show_main, show_product, show_xml, show_json, show_json_by_id, show_xml_by_id, delete_item, register, login_user, logout_user, show_shop

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('items/create/', create_items, name='create_items'),
    path('items/<int:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('items/<int:id>/delete/', delete_item, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('shop/', show_shop, name='show_shop'),
]