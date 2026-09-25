from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comunicados/<int:pk>/', views.comunicado_detalle, name='comunicado_detalle'),
    path('login/', views.IntranetLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
