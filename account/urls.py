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
    # path('', views.TempView.as_view(), name='home'),
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.MySignupView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    # path('user/', views.MyUserView.as_view(), name='user'),
    # path('other/', views.MyOtherView.as_view(), name='other'),
]
