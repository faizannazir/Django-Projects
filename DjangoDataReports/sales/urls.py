from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('',views.home,name="home"),
    path('sales/',views.SalesListView.as_view(),name="salesList"),
    path('sales/<pk>/',views.SalesDetailView.as_view(),name="saleDetail"),
]
