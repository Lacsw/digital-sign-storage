from django.urls import path

from . import views
from .views import CustomerList, CustomerUpdateView, CustomerDetailView, SignList

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('detail', CustomerList.as_view(), name='customer_list'),
    path('detail/<pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:id>/delete', views.quote_delete, name='quote_delete'),
    path('detail/<int:pk>/update',
         CustomerUpdateView.as_view(), name='customer_update'),
    path('sign/create/', views.sign_create, name='sign_create'),
    path('sign/list', SignList.as_view(), name='sign_list'),

]
