from django.urls import path
from . import views

app_name = 'spelsberg'

urlpatterns = [
    path('', views.product_list, name='spelsberg_lists'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='spelsberg_detail')

]
