from django.urls import path
from . import views
from . import getUserInfo
from django.conf.urls import include

app_name = 'api'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('barcode/', views.ShowBarcode.as_view()),
    path('info/', getUserInfo.GetInfo.as_view())
]
