from django.urls import path
from . import views
from . import getRepoInfo
from django.conf.urls import include


app_name = 'api'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('barcode/', views.barcode),
    path('info/', getRepoInfo.GetInfo.as_view()),
]
