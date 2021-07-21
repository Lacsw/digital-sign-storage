from django.urls import path

from . import views
from .views import QuoteList, QuoteUpdateView, QuoteView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('detail/<int:pk>', QuoteView.as_view(), name='quote-detail'),
    path('detail', QuoteList.as_view(), name='detail-quotes'),
    path('<int:id>/delete', views.quote_delete, name='quote_delete'),
    path('detail/<int:pk>/update', QuoteUpdateView.as_view(), name='quote_update')
]