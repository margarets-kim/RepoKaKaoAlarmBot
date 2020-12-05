from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'api'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('barcode/', views.barcode),
    path('repoList/', views.repoList),
    path('repoStatus/', views.repoStatus),
    path('info/', views.GetRepoInfo.as_view()),
    path('alias/', views.SendAlias.as_view())
]
