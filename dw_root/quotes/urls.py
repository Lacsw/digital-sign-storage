from django.urls import path

from . import views
from .views import CustomerList, CustomerUpdateView, CustomerDetailView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('detail', CustomerList.as_view(), name='customer-list'),
    path('detail/<pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:id>/delete', views.quote_delete, name='quote_delete'),
    path('detail/<int:pk>/update', CustomerUpdateView.as_view(), name='quote_update'),
    path('sign/create/', views.sign_create, name='sign_create'),

]