from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.say_hello),
    #path('',views.home, name='home'),
    path('success/', views.success, name='success'),
    path('', views.displaysubscription, name='subscription'),
    path('pay/<int:subscription_id>', views.payment, name='pay'),
    path('confirmation', views.confirmation, name='confirmation')

]
