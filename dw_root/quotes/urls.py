from django.urls import path

from quotes.views import *
from . import views


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
    path('sign/<int:pk>/delete', SignDeleteView.as_view(), name='sign_delete'),
    path('sign/7days_left', Sign7DaysList.as_view(), name='sings_7days_left'),
    path('sign/15days_left', Sign15DaysList.as_view(), name='sings_15days_left'),
    path('sign/30days_left', Sign30DaysList.as_view(), name='sings_30days_left'),
    
]
