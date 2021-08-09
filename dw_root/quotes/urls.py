from django.urls import path

from . import views
from .views import CustomerList, CustomerUpdateView, CustomerView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('detail/<int:pk>', CustomerView.as_view(), name='quote-detail'),
    path('detail', CustomerList.as_view(), name='detail-quotes'),
    path('<int:id>/delete', views.quote_delete, name='quote_delete'),
    path('detail/<int:pk>/update', CustomerUpdateView.as_view(), name='quote_update')
]