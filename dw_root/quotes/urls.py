from django.urls import path

from . import views
from .views import QuoteList, QuoteUpdateView, QuoteView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show/<int:pk>', QuoteView.as_view(), name='quote-detail'),
    path('show', QuoteList.as_view(), name='show-quotes'),
    path('<int:id>/delete', views.quote_delete, name='quote_delete'),
    path('show/<int:pk>/update', QuoteUpdateView.as_view())
]