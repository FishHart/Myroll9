# from django.urls import path, include
# from . import views


# app_name ='account'

# urlpatterns = [
#     path('', views.TopView.as_view(), name='top'),
# ]

"""accountのURL定義"""
from django.urls import path
from .apps import AccountConfig
from . import views

app_name = AccountConfig.name # accountが入る
urlpatterns = [
    path('', views.TempView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
]
