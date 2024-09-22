from django.contrib import admin
from django.urls import path, include
from orders import views
from django.contrib.auth import views as auth_views
from orders.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('landing/', views.landing_page, name='landing_page'),
    path('new_order/', views.new_order, name='new_order'),
    path('track_orders/', views.track_orders, name='track_orders'),
    path('order/<int:order_id>/mark_received/', views.mark_received, name='mark_received'),
    path('order/<int:order_id>/mark_approved/', views.mark_approved, name='mark_approved'),
    path('order/<int:order_id>/mark_arrived/', views.mark_arrived, name='mark_arrived'),
    path('logout/', logout_view, name='logout'),  # הפניה לפונקציה שלך
]