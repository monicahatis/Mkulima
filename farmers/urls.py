from django.urls import path
from . import views


app_name = 'farmers'

urlpatterns = [
    path('', views.IndexView.as_view(), name='farmers'),
    path('add/', views.AddView.as_view(), name='add-farmer'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('<slug:pk>/', views.SingleView.as_view(), name='details-farmers'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit-farmer'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete-farmer'),
]
