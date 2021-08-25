from django.urls import path

from . import views
from .views import CustomerDeleteView, CustomerList, CustomerUpdateView, CustomerDetailView, SignList, SignUpdateView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('detail', CustomerList.as_view(), name='customer_list'),
    path('detail/<pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
    path('detail/<int:pk>/update',
         CustomerUpdateView.as_view(), name='customer_update'),
    path('sign/create/', views.sign_create, name='sign_create'),
    path('sign/list', SignList.as_view(), name='sign_list'),
    path('sign/<int:pk>/update',
         SignUpdateView.as_view(), name='digitalSign_update'),


]
