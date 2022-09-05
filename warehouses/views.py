from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from farmer_connections.models import Farmer_WH_Owner_Connection
from farmer_connections.serializers import FarmerConnectionsSerializer
from warehouses.forms import CommunicationsForm, WarehouseCreationForm, WarehouseUpdateForm
from django.contrib import messages
from warehouses.models import Warehouses
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def warehouses(request):
    warehouses = Warehouses.objects.all()
    return render(request, "warehouses/warehouses.html", {'warehouses': warehouses})


@login_required
def add_warehouse(request):
    if request.method == "POST":
        form = WarehouseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            messages.success(request, "warehouse upload success")
            return redirect("home")
    else:
        form = WarehouseCreationForm()
    return render(request, "warehouses/add_warehouse.html", {'form': form})


@login_required
def my_warehouses(request):
    warehouses = Warehouses.objects.filter(user=request.user)
    return render(request, 'warehouses/my-warehouses.html', {'warehouses': warehouses})


@login_required
def delete_warehouse(request, id):
    warehouse = get_object_or_404(Warehouses, pk=id)
    warehouse.delete()
    return redirect("index")


def details_warehouse(request, id):
    warehouse = get_object_or_404(Warehouses, pk=id)
    return render(request, "warehouses/details.html", {'upload': warehouse})


@login_required
def edit_warehouse(request, id):
    warehouse = get_object_or_404(Warehouses, pk=id)
    if request.method == "POST":
        form = WarehouseUpdateForm(
            request.POST, request.FILES, instance=warehouse)

        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            messages.success(request, "warehouse update success")
            return redirect("home")
    else:
        form = WarehouseUpdateForm(instance=warehouse)
    return render(request, "warehouses/edit-warehouse.html", {'form': form})

@login_required
@api_view(["GET","POST"])
def new_message(request):
    if request.method == "POST":
        serializer = FarmerConnectionsSerializer(data=request.data, initial={'wh_owner_id': request.user})
        if serializer.is_valid():
            serializer.save()
            return redirect("all-messages")
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        messages.success(request, "message sending failed")
    else:
        form = CommunicationsForm(initial={"wh_owner_id": request.user})
    return render(request, "warehouses/new_message.html", {'form': form})

def all_message(request):
    snippets = Farmer_WH_Owner_Connection.objects.all()
    return render(request, "warehouses/all-messages.html", {'communications': snippets})