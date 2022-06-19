# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.myroll, name='myroll'),
# ]

"""myrollのURL定義"""
from django.urls import path
from .apps import MyrollConfig
from . import views as myrollView

app_name = MyrollConfig.name # myrollが入る
urlpatterns = [
    path('', myrollView.myroll.as_view(), name='home'),
]
