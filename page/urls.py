from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'page'
urlpatterns = [
    path('', views.KakaoInfo.as_view()),
]
