from warehouses import views
from django.urls import path

urlpatterns = [
    path("", views.warehouses, name="warehouse"),
    path("add-warehouse/", views.add_warehouse, name="add-warehouse"),
    path('edit_warehouse/<int:id>/', views.edit_warehouse, name="edit_warehouse"),
    path('delete_warehouse/<int:id>/',
         views.delete_warehouse, name="delete_warehouse"),
    path('my_warehouses/', views.my_warehouses, name='my_warehouses'),
    path('details_warehouse/<int:id>/',
         views.details_warehouse, name='details-warehouse'),
    path("new-message/", views.new_message, name="new-message"),
    path("all-messages/", views.all_message, name="all-messages"),
]
