from django.urls import path
from main.views import (
    create_items, show_main, show_product, show_xml, show_json,
    delete_item, register, login_user, logout_user, 
    edit_product, show_navbar, get_product_json, add_product_ajax, update_product_ajax, 
    delete_product_ajax, login_ajax, register_ajax, logout_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('items/create/', create_items, name='create_items'),
    path('items/<int:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('items/<int:id>/delete/', delete_item, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('navbar/', show_navbar, name='show_navbar'),
    
    path('get-product/<int:id>/', get_product_json, name='get_product_json'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('update-product-ajax/<int:id>/', update_product_ajax, name='update_product_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('logout-ajax/', logout_ajax, name='logout_ajax'),
]