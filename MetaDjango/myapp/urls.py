from django.urls import path

from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('myview',views.MyView.as_view(),name="classview")
]