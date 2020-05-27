from django.urls import path
from myapp import views

app_name='myapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    ]
